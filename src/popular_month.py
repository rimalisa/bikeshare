import time
import csv
import pprint
import datetime
import pandas as pd
import numpy as np
import collections

## Filenames
chicago = '../data/chicago.csv'
new_york_city = '../data/new_york_city.csv'
washington = '../data/washington.csv'

CITY_DATA = {'chicago': '../data/chicago.csv',
             'new york city': '../data/new_york_city.csv',
             'washington': '../data/washington.csv' }

def popular_month(city_file):
 #   '''TODO: fill out docstring with description, arguments, and return values.
  #  Question: What is the most popular month for start time?
   # '''
    # TODO: complete function

#read the file from CSV
    city_file = pd.read_csv(city_file)

# get the start time month from the Start time column
    start_time_month=[]
    for i in range(len(city_file)):
         start_time_month.append(int(city_file.loc[i, 'Start Time'].split()[0].split("-")[1]))

# count each month's number of occurences and put it in a dict
    start_time_month_counter= collections.Counter(start_time_month)
    print(start_time_month_counter)
# get the max of the dict
    maximum = max(start_time_month_counter, key=start_time_month_counter.get)
    print(maximum)
    if maximum == 1: print("January is the month that occurs most often in the start time ")
    elif maximum == 2: print("February is the month that occurs most often in the start time ")
    elif maximum==3: print("March is the month that occurs most often in the start time ")
    elif maximum==4: print("April is the month that occurs most often in the start time ")
    elif maximum==5: print("May is the month that occurs most often in the start time ")
    else: print("June is the month that occurs most often in the start time ")


if __name__ == "__main__":
    popular_month(washington)