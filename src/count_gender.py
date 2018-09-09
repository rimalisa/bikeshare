## TODO: import all necessary packages and functions
import time
import csv
import pprint
import datetime
import pandas as pd
import numpy as np
import collections

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

CITY_DATA = {'chicago': '../data/chicago.csv',
             'new york city': '../data/new_york_city.csv',
             'washington': '../data/washington.csv'}


def gender(df, city):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    counts the number of male and female

    Args:
        (str) city - name of the city to analyze
        (data frame) df - the data frame after the use of filter on month and day and city
    Returns:
        (list) list_gender - count of genders
    '''
    # TODO: complete function

    if city == 'Washington' or city== "washington":
        print('There is no available gender data for this city')
        list_gender=' '
    else: list_gender= df['Gender'].value_counts()

    return list_gender

if __name__ == "__main__":
    print(gender(df, 'washington'))
