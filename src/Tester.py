def get_city() -> object:
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    if city not in ['chicago', 'Chicago', 'washington', 'Washington', 'new york city', 'New york city']:
        print('please choose between : chicago, washington, or new york city!')
        get_city()
    print(city)
    return city

if __name__ == "__main__":
	get_city()
