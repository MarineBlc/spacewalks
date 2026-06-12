import json
import csv
import datetime as dt
import matplotlib.pyplot as plt

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding="ascii")
output_file = open('./eva-data.csv','w', encoding="utf-8")
graph_file = './cumulative_eva_graph.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

data=[]

for i in range(375):
    line=input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet

processed_data=csv.writer(output_file)

time = []
date =[]

line=0
for i in data:
    print(data[line])
    # and this bit
    processed_data.writerow(data[line].values())
    if 'duration' in data[line].keys():
        duration_str=data[line]['duration']
        if duration_str == '':
            pass
        else:
            duration_dt=dt.datetime.strptime(duration_str,'%H:%M')
            duration_hours = dt.timedelta(hours=duration_dt.hour, minutes=duration_dt.minute, seconds=duration_dt.second).total_seconds()/(60*60)
            print(duration_dt,duration_hours)
            time.append(duration_hours)
            if 'date' in data[line].keys():
                date.append(dt.datetime.strptime(data[line]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[line]['date'][0:10])

            else:
                time.pop(0)
    line+=1

t=[0]
for i in time:
    t.append(t[-1]+i)

date,time = zip(*sorted(zip(date, time)))


plt.plot(date,t[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
