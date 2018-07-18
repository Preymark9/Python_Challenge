import os
import csv

csvpath = r"C:\Users\major\OneDrive\Documents\WASHSTL201806DATA4-Class-Repository-DATA\Week 3 - Python\Homework\PyPoll\Resources\election_data.csv"
with open(csvpath, "r") as csvfile:
    #who are the candidates
    #who got the most votes
    #who got the least votes
    #tally the votes for everyone
    csvreader = csv.reader(csvfile)
    print(csvreader)
    votes = []
    for tally in csvreader:
        if tally[0] != "Voter ID":
            votes.append(str(tally[0]))
print("number of voters is", len(votes))