#'''Asks the user for a time period and returns the specified filter.

#   Args:
 #      none.
  # Returns:
   #    TODO: fill out return type and description (see get_city for an example)
   #'''
time_period = input('\nWould you like to filter the data by month, day, or not at'
                    ' all? Type "none" for no time filter.\n')
# TODO: handle raw input and complete function

if time_period == 'day':
    time_period = input('\nPlease select the day of the week: Sun, Mon, Tue, Wed, Thu, Fri, Sat.\n')
elif time_period == 'month':
    time_period= input('\nPlease type in the month: Jan, Feb, Mar, Apr, May, Jun.\n')
elif time_period == 'none': input('\nAlright, you did not select any filter \n')
else: input('\n Please choose a valid filter; day, month or none !\n ')

print(time_period)