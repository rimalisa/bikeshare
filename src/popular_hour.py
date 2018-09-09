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

# TODO: complete function
#import city file from csv to dataframe
df_city = pd.read_csv(washington)
# convert the Start Time column to datetime
df_city['Start Time'] = pd.to_datetime(df_city['Start Time'])
def hr_func(ts):
    return ts.hour
# extract hour from the Start Time column to create an hour column
df_city['hour'] = df_city['Start Time'].apply(hr_func)
# find the most common hour (from 0 to 23)
popular_hour = df_city['hour'].mode()[0]
print('Most Frequent Start Hour:', popular_hour)