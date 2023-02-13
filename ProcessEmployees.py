'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iterate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file

infile = csv.reader(open("employee_data.csv"))
next(infile)


# create an empty dictionary

new_dictionary = {}

# use a loop to iterate through the csv file


for i in infile:
    # check if the employee fits the search criteria
    # new_dictionary[i[1]] = i[5]
    # print(new_dictionary)
    if i[3] == "Marketing":
        if i[4] == "CSR":
            print(f"Manager Name: {i[1]} {i[2]} Current Salary: {i[5]}")
            new_dictionary[f"{i[1]} {i[2]}"] = float(i[5])*1.1

print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout
for i in new_dictionary:
    print(f"Manager Name: {i} New Salary: {new_dictionary[i]}")
