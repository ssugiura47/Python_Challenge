import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

print("Electrion Results")

#The total number of votes cast
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    for row in csvreader:
        row_count = sum(1 for row in csvreader)
    print("Total number of votes: " + str(row_count))

#A complete list of candidates who received votes
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) 
    candidatelist = []
    for row in csvreader:
        if row[2] not in candidatelist:
            candidatelist.append(row[2])
    print(f"The candidates are: {candidatelist} ")

#The total number of votes each candidate won
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) 
    vote_Khan = 0
    for row in csvreader:
        if row[2] == "Khan":
            vote_Khan = vote_Khan + 1
            vote_Khan_percent = (vote_Khan)/(row_count)*100
            vote_Khan_result = round(vote_Khan_percent, 2)          
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) 
    vote_Correy = 0
    for row in csvreader:
        if row[2] == "Correy":
            vote_Correy = vote_Correy + 1
            vote_Correy_percent = (vote_Correy)/(row_count)*100
            vote_Correy_result = round(vote_Correy_percent, 2)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) 
    vote_Li = 0
    for row in csvreader: 
        if row[2] == "Li":
            vote_Li = vote_Li + 1
            vote_Li_percent = (vote_Li)/(row_count)*100
            vote_Li_result = round(vote_Li_percent, 2)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader) 
    vote_OTooley = 0
    for row in csvreader: 
        if row[2] == "O'Tooley":
            vote_OTooley = vote_OTooley + 1 
            vote_OTooley_percent = (vote_OTooley)/(row_count)*100
            vote_OTooley_result = round(vote_OTooley_percent, 2)
         

print(f"Khan has {vote_Khan_result} percent of the votes!") 
print(f"Correy has {vote_Correy_result} percent of the votes!") 
print(f"Li has {vote_Li_result} percent of the votes!")  
print(f"O'Tooley has {vote_OTooley_result} percent of the votes!")  

if vote_Khan_result > (vote_Correy_result and vote_Li_result and vote_OTooley_result):
    print("The winner is Khan!")
elif vote_Correy_result > (vote_Khan_result  and vote_Li_result and vote_OTooley_result):
    print("The winner is Correy!")
elif vote_Li_result > (vote_Khan_result and vote_Correy_result and vote_OTooley_result):
    print("The winner is Li!")
elif vote_OTooley_result > (vote_Khan_result and vote_Correy_result and vote_Li_result):
    print("The winner is O'Tooley!")

user = input("Who won?")

write_file = open(os.path.join("Analysis", "pypoll_results.txt"), 'w+')
write_file.write(f"Total number of votes: {row_count}")
write_file.write(f", The candidates are: {candidatelist}")
write_file.write(f", Khan has {vote_Khan_result} percent of the votes!") 
write_file.write(f", Correy has {vote_Correy_result} percent of the votes!") 
write_file.write(f", Li has {vote_Li_result} percent of the votes!")
write_file.write(f", O'Tooley has {vote_OTooley_result} percent of the votes!")
write_file.write(f", The winner is {user}!")