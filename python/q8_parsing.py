#The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv
#assigning dictionary reader to create a dictionary
f_dict = csv.DictReader(open('/Users/natalieabril/ds/metis/prework/dsp/python/football.csv'))
team = ''
min_diff = 0
for row in f_dict:
    goals = int(row['Goals'])
    goals_allowed = int(row['Goals Allowed'])
    diff = abs(goals - goals_allowed)
    if min_diff == 0 or min_diff > diff:
        min_diff = diff
        team = row['Team']
print '%s has the smallest difference of goals. Difference = %d' %(team, min_diff)

#I did not utilize the functions below
  def read_data(data):
   # COMPLETE THIS FUNCTION

  def get_min_score_difference(self, parsed_data):
    # COMPLETE THIS FUNCTION

  def get_team(self, index_value, parsed_data):
    # COMPLETE THIS FUNCTION
