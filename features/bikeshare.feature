Feature: Bike share application to query usage of bikes
  As a data scientist
  I should be able to monitor ride share stations

Background:
 Given a File named "Data/chicago.csv" containing the rideshare data for the city of "chicago" defined by columns
   | startTime |
   | endTime   |


Scenario: Find most used start station for a given day
Given a city named "Chicago"
When I ask my program to give me the the most used start station for a given day "monday"
Then I should obtain a valid station

Scenario: find the month that occurs the most often in the start time
Given a city: chicago, New york or Washington
When I ask my program to give me the month that occurs the most often in the start time
my program will go through the start_date column and get all the counts of each month
it will put the count in a counter ( a dictionary ),we take the max of the counter
Then I should obtain the most popular month

Scenario: Find most popular day of week (Monday, Tuesday, etc.) for start time
Given a city, a month , and a day
When I ask my program to give me the most popular day of the week during a month in the start time field.
Then I should get the average of each day of the week for this month