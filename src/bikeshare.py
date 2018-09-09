## TODO: import all necessary packages and functions
import time
import datetime
import pandas as pd
import collections

## Filenames
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

CITY_DATA = {'chicago': '../data/chicago.csv',
             'new york city': '../data/new_york_city.csv',
             'new york': '../data/new_york_city.csv',
             'washington': '../data/washington.csv'}

def get_city() -> object:
    '''Asks the user for a city and returns the filename for that city's bike share data.
    the function checks the validity of the input

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    # TODO: handle raw input and complete function



    selection = input('\nHello! Let\'s explore some US bikeshare data!\n'
                      'Would you like to see data for Chicago, New York, or Washington?\n')
    selection = selection.lower()
    while selection not in ['chicago', 'washington','new york city', 'new york']:
        print ("Please enter a valid city!")
        selection = input('Would you like to see data for Chicago, New York, or Washington?\n')

    city = selection.lower()


    return city

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.
    the function checks the validity of the input
    Args:
        none.
    Returns:
        (str) object with a selected time period.
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    # TODO: handle raw input and complete function
    time_period = time_period.lower()
    if time_period not in ['month', 'day', 'none' ]:
        input('\n Please choose a valid filter; day, month or none \n ')
    return time_period

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        (str) object with the month for the filter
    '''
    month = input('\nWhich month? Jan, Feb, Mar, Apr, May, or Jun?\n')
    month = month.lower()
    if month == 'january':
        month = 'jan'
    elif month == 'february':
        month = 'feb'
    elif month == 'march':
        month = 'mar'
    elif month == 'april':
        month = 'apr'
    elif month == 'june':
        month = 'jun'
    elif month in ['jan', 'feb', 'mar', 'apr', 'may','jun']:
        month == month
    else:
        print('Please enter a valid month : Jan, Feb, Mar, Apr, May, or Jun')


    return month

def get_day():
    '''Asks the user for a day and returns the specified day.
    the function checks if the input is valid
    Args:
        none.
    Returns:
        (str) object with a day for the filter
    '''

    selection = input('\nWhich day? Please type : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n')
    selection = selection.lower()
    while selection not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','mon', 'tue', 'wed', 'thu','fri','sat', 'sun']:
        print("Please enter a valid day!")
        selection = input('\nWhich day? Please type : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n')

    day = selection.lower()
    if day == 'mon':
        day = 'monday'
    elif day == 'tue':
        day = 'tuesday'
    elif day == 'wed':
        day = 'wednesday'
    elif day == 'thu':
        day = 'thursday'
    elif day == 'friday':
        day = 'fri'
    elif day == 'sat':
        day = 'saturday'
    else:
        if day == 'sun':
            day = 'sunday'
    return day


def popular_month(city):
    """
     Question: What is the most popular month for start time?
     args: (str) the city selected by the user
     returns : none

    """
    # read the file from CSV
    city_file = pd.read_csv(CITY_DATA[city])

    # get the start month from the Start time column
    start_time_month=[]
    for i in range(len(city_file)):

        start_time_month.append(int(city_file.loc[i, 'Start Time'].split()[0].split("-")[1]))

    # count each month's number of occurences and put it in a dict
    start_time_month_counter = collections.Counter(start_time_month)
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
    #df['month'] = df['month'].str.lower()
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #df['day_of_week'] = df['day_of_week'].str.lower

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def popular_day(df):

    """
        this function takes the dataframe already filtered and extracts the most popular day using the mode
        Question: What day of the week (Monday, Tuesday, etc.) occurs most often in the start time?
        args: pandas dataframe already filtered
        returns : none
    """
    # find the most popular day
    popular_days = df['day_of_week'].mode()[0]
    print('Most popular day:', popular_days)


def hr_func(ts):
    return ts.hour

def popular_hour(df):
    '''
    Question: What hour of the day (0, 2, ... 22, 23) occurs most often in the start time?
    args: pandas dataframe already filtered
    returns: none
    '''


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    def hr_func(ts):
        return ts.hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].apply(hr_func)
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

def trip_duration(df):
    '''
    args :
        df: the filtered data frame
    returns:sum and average of trip duration
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    sum_trip_duration = df['Trip Duration'].sum()
    avg_trip_duration = df['Trip Duration'].mean()
    print('Total Trip duration in seconds:', sum_trip_duration)
    print('Average Trip duration in seconds:', avg_trip_duration)
    return sum_trip_duration, avg_trip_duration


def popular_stations(df):
    '''
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
    print('The most popular start station is :', popular_start_station)
    print('The most popular end station is :', popular_end_station)



def popular_trip(df):
    '''
    Question: What is the most common trip (i.e., the combination of start station and
    end station that occurs the most often)?


    prints the most popular combination for a start and end station
    Args:
        (data frame) df is a filtered data frame
    Returns:
        none,
    '''


    # group by the combination of end and start station, and count the combination with the most occurrences
    most_popular_trips = (
    df.groupby(['Start Station', 'End Station']).size().reset_index().rename(columns={0: 'count'}))

    most_popular_trip_index = max(most_popular_trips['count'])

    message = "The most popular trip is : {} as start station and {} as end station with a total of {}\n"

    print(message.format(most_popular_trips.at[most_popular_trip_index, 'Start Station'],
                         most_popular_trips.at[most_popular_trip_index, 'End Station'], most_popular_trip_index))


def users(df):
    '''
    Question: What are the counts of each user type?
    args: the pandas dataframe df already filtered
    returns: a list of user types
    '''


    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)
    return user_types

def gender(df, city):
    '''
    Question: What are the counts of gender?
    counts the number of male and female

    Args:
        (str) city - name of the city to analyze
        (data frame) df - the data frame after the use of filter on month and day and city
    Returns:
        (list) list_gender - count of genders
    '''


    if city == 'Washington' or city== "washington":
        print('There is no available gender data for this city')
        list_gender =' '
    else:
        list_gender = df['Gender'].value_counts()
        print(list_gender)
    return list_gender




def birth_years(df,city):
    '''
    Question: What is the earliest birth year (when the oldest person was born),
    most recent birth year, and most common birth year?
    args: the pandas dataframe already filtered
          (str) the city selected by the user
    returns: none
    '''


    if city == 'Washington' or city== "washington":
        print('There is no available birth data for this city')

    else:
        df = df.dropna(axis=0, how ='any')
        common_birth_year = df['Birth Year'].mode()
        oldest_birth_year = df['Birth Year'].min()
        recent_birth_year = df['Birth Year'].max()
        print('The most commom birth year is :', int(common_birth_year))
        print('The oldest birth year is :', int(oldest_birth_year))
        print('The most recent birth year is :', int(recent_birth_year))





def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()


    # Filter by time period (month, day, none)
    time_period = get_time_period()
    if time_period == 'none' or time_period == 'None':
        print('Alright, you did not select any filter ')
        month = 'all'
        day = 'all'
    elif time_period == 'month':
        month = get_month()
        day = 'all'
    else:
        day = get_day()
        month = 'all'
    df = load_data(city, month, day)
    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none' or time_period == 'None':
        start_time = time.time()

        #TODO: call popular_month function and print the results
        popular_month(city)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()

        # TODO: call popular_day function and print the results

        popular_day(df)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results

    print("The most popular hour of the day:", popular_hour(df))
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(df)

    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
    popular_stations(df)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(df)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    print('The count of each user type :')
    users(df)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    gender(df,city)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    birth_years(df,city)
    print("That took %s seconds." % (time.time() - start_time))


    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()
