# Spacewalks

## Overview
Code made to analyse eva data from an eva-data.json file, save the processed output in a eva-data.csv, and plot the the total time spent in space per year.

## Pre-requisites
    - pyhton 3.12
    - matplotlib >= 3.11.0
    - pandas >= 3.0.3
    - pytest >=9.1.1
To install all required packages to run the code, see installation instructions below.

## Installation
-  Use git clone to copy the code and project structure
- Create a new environment for the code venv_spacewalks with:
```bash
python3 -m venv venv_spacewalks
``` 
and activate the environement with:
On MAC:
```bash
    source venv_spacewalks/bin/activate 
``` 
On Windows:
```bash
    source venv_spacewalks/Script/activate
``` 
Then install the dependencies from the requirements.txt file with:
```bash
    python3 -m pip install -r requirements.txt
``` 

## Usage
Run the code by running the command line:
```bash
python eva_data_analysis.py ./name_of_input.json ./name_of_output.csv
```  
The input file should be in a data folder. It will create an output file and figure in the results folder.