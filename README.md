## PyBank ##

Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset
# count the number or rows in the data but using the sum function for every row using for loop

The net total amount of "Profit/Losses" over the entire period
# find the profit/losses between two rows and appending it to a list (reminder: we will need to remove the first number in the list because it's essentially grabbing the difference between the first number in the data and 0), then adding them up

The average of the changes in "Profit/Losses" over the entire period
# using the net total determined above, find out how many items in the list of profit/losses there were and divide net total by number of items

The greatest increase in profits (date and amount) over the entire period
# using a for loop, find the max number by replacing the set max number if profit is greater than the current max number

The greatest decrease in losses (date and amount) over the entire period
# using a for loop, find the min number by replacing the set min number if profit is less than the current min number


## PyPoll ##

You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

The total number of votes cast
# count the number or rows in the data but using the sum function for every row using for loop

A complete list of candidates who received votes
# using a for loop, loop through the data row by row and look at index 2 (Candidate column). create an empty list and if that value in index 2 is no in the list, add to list

The percentage of votes each candidate won
# using an if statement, add to sum of votes for each candidate. using the total number of votes we determined above, find the percentage

The total number of votes each candidate won
# this can be combine with the previous step

The winner of the election based on popular vote.
# using an if statement, set up a winner and if the number of votes for a candidate is greater than the winner, replace the winner