1. Pseudo code for bike sharing program


Background:
 Given a File named "Data/chicago.csv" containing the rideshare data for the city of "chicago" defined by columns
   | startTime |
   | endTime   |
 

Scenario: Find most used start station for a given day
Given a city "Chicago"
When I ask my program to give me the the most used start station for a given day "monday"
Then I should obtain a valid station


function2:
Scenario: find the month that occurs the most often in the start time 
Given a city: chicago, New york or Washington
when I ask my program to give me the month that occurs the most often in the start time
my program will go through the start_date column and get all the counts of each month
it will put the in a counter, (probably a dictionary )
we take the max of the counter 
Then I should obtain a month


# What is the most popular day of week (Monday, Tuesday, etc.) for start time?