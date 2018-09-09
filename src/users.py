
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

# load data file into a dataframe
df = pd.read_csv(filename)

# print value counts for each user type
user_types = df['User Type'].value_counts()

print(user_types)