"""
The script reads the data from a JSON file, processes it, and outputs a CSV file and a graph of cumulative EVA time over the years.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Define input and output file paths
# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding="ascii")
output_file = open('./eva-data.csv','w', encoding="utf-8")
graph_file = './cumulative_eva_graph.png'

# Load the data with pandas, converting the date column to datetime objects
eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
eva_df['eva'] = eva_df['eva'].astype(float)
eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True)

# Save the processed data to a CSV file
eva_df.to_csv(output_file, index=False, encoding='utf-8') 

# Sort dates
eva_df.sort_values(by='date', inplace=True)

# Create a cumulative time of EVA 
eva_df['duration_hours'] = eva_df['duration'].str.split(':').apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# Plot the cumulative time spent in space over the years
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
