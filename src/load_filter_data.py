## TODO: import all necessary packages and functions
import time
import csv
import pprint
import datetime
import pandas as pd
import numpy as np
import collections
import pandas as pd

CITY_DATA = {'chicago': '../data/chicago.csv',
             'new york city': '../data/new_york_city.csv',
             'washington': '../data/washington.csv'}


def load_data(city: object, month: object, day: object) -> object:
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        print(df)
    return df


df = load_data('washington', 'may', 'tuesday')

#print(df.head())


def popular_stations(df):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most frequently used start station and most frequently
    used end station?
    this function select the most popular station for the start time and end time using a given city, month, and day
    args:
        df: filtered dataframe
    return:
        none
    '''
    # TODO: complete function
    # getting the most frequent start and end station
    popular_start_station_index = max(df['Start Station'].value_counts())
    popular_end_station_index = max(df['End Station'].value_counts())
    # getting the name of the most used start and end stations using the index location
    popular_start_station = df.iloc[popular_start_station_index][ 'Start Station']
    popular_end_station = df.iloc[popular_end_station_index]['End Station']
    print(popular_start_station)
    print(popular_end_station)

if __name__ == "__main__":
    popular_stations(df)
