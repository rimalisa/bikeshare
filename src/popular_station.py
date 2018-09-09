
## TODO: import all necessary packages and functions
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
filename = chicago


def popular_stations(df):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most frequently used start station and most frequently
    used end station?
    '''
    # TODO: complete function
    # load data file into a dataframe
    #df = pd.read_csv(filename)

    # print value counts for each user type
    popular_start_station_index = max(df['Start Station'].value_counts())
    popular_End_station_index = max(df['End Station'].value_counts())
    popular_start_station = df.at[most_popular_trip_index, 'Start Station']
    popular_end_station = df.at[most_popular_trip_index, 'End Station']
    print(popular_start_station)
    print(popular_end_station)
