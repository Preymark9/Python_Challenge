import os
import csv

csvpath = r"C:\Users\major\OneDrive\Documents\WASHSTL201806DATA4-Class-Repository-DATA\Week 3 - Python\Homework\PyBank\Resources\budget_data.csv"
with open(csvpath, "r") as csvfile:
    #find the highest value on the revenue column
    #also find the lowest value on the revenue column
    #what was the biggest growth in a month?
    #what the biggest loss in a month?
    #what average profit or loss?
    csvreader = csv.reader(csvfile)
    print(csvreader) #I want it to read me the highest value
    for data in csvreader:
        print(data[1])
