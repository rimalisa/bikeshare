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


def get_city() -> object:
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    # TODO: handle raw input and complete function
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    city = city.lower()
    print('in',city)
    if city not in ['chicago', 'Chicago', 'washington', 'Washington', 'new york city', 'New york city', 'new york',
                    'New york']:
        print('please choose between : chicago, washington, or new york city')
        get_city()

    return city

if __name__ == "__main__":
	print(get_city())
