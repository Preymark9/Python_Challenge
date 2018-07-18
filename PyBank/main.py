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
    print(csvreader) #I want it to read me the highest value\
    #print as list revenue = [csvreader(1)]
    revenue = []
    for data in csvreader:
        #input max of a list in the revenue
        #revenue.append(data[1])
        #print(data[1])
        #print(max(revenue))
        #print(revenue)
        if data[1] != "Revenue": 
            revenue.append(int(data[1]))
        #Else if data == int: 
            #print("the max is", max(revenue))
print(revenue)
print("the number of months is", len(revenue))
print("the max  is ", max(revenue))
print("the mix is ", min(revenue))