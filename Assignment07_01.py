# ---------------------------------------------------------------------------- #
# Title: Assignment 07 Pickling
# Description: Script to act as instruction for creating a working script for
#              pickling.
# ChangeLog (Who,When,What):
# IMarhsall,2.26.2023,Created started script for Assignment07
# ---------------------------------------------------------------------------- #

# Declare variable------------------------------------------------------------ #
intPhone = ''  # User defined integer representing a phone number
strname = ''  # User defined string representing a person's name
lstcustomer = []  # A list that acts as a collection of customer info


# Simple code one: Pickling - Pickling converts any Python object (list, dict, etc.)
#                   into binary. This allows for easier transfer between databases
#                   to then be stored in a file or database.

import pickle  # Imports code from another file

strname = str(input('Please enter a first and last name: ').strip())
intPhone = int(input('Please enter a phone number: ').strip())
lstcustomer = [strname, intPhone]
'''print(lstcustomer)'''
# Duplicated print to user with print(objFileData below, removed to clean visual

# We will use pickle.dump to store the data, it works the same as writing the data to a file, just lets the system
# know it's binary.
objfile = open('CustomerContact.txt', 'ab')
# 'ab' appends the data in the file, allowing us to add to it without overriding it while defining it as binary.
pickle.dump(lstcustomer, objfile)
objfile.close()

# To verify the data saved we will read back the data contained in it with pickle.load
objFile = open("CustomerContact.txt", "rb")
objFileData = pickle.load(objFile) #load() only loads one row of data.
objFile.close()

print(objFileData)

