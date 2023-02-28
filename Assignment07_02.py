# ---------------------------------------------------------------------------- #
# Title: Assignment 07 Exception Handling
# Description: Script to act as instruction for creating a working script for
#              pickling and exception handling.
# ChangeLog (Who,When,What):
# IMarhsall,2.26.2023,Created started script for Assignment07
# IMarhsall,2.26.2023,Added script to Assignment 07 Pickling.py to add parameters and exception handling
# ---------------------------------------------------------------------------- #

# Declare variable------------------------------------------------------------ #
strPhone = ''  # User defined string to check length prior to converting to integer
intPhone = ''  # User defined integer representing a phone number converted from strPhone
strname = ''  # User defined string representing a person's name
lstcustomer = []  # A list that acts as a collection of customer info
lstcustFile = []  # Memory load of all data in CustomerContact.txt


# Simple code two: Exception Handling - We are building on the code from Assignment 07 Pickling
#                   to show ways to handle common exceptions that may occur during user interfaces
#                   using try/catch blocks to allow the program to continue without completely breaking
#                   when an error is encountered


import pickle  # Imports code from another file

while True:
    strname = str(input('Please enter a first and last name: ').strip())
    # A simple way to help mitigate people only entering their first name is to have the program check to see
    # that the entry contains a space.
    if ' ' not in strname:
        print('Invalid, please ensure you are entering your first AND last name.')
    else:
        break
while True:
    strPhone = str(input('Please enter a domestic phone number with area code (numbers only): ').strip())
    if len(strPhone) != 10:
# In the last program the user could enter any number they wanted
# and if anything was entered that wasn't a number the program would break. To prevent this we did the following:
#   Checks to make sure that there are 10 characters entered
#   Changed to start as string and check for length first, making sure user enters full phone number length
#   Then become integer and check to see if data are numbers,
#   since data entry didn't recognize 0 as an integer if user entered it intitially
        print('Invalid phone number length. Please enter a 10 digit phone number.')
    else:
        try:
            intPhone = int(strPhone)
            break
        except ValueError as ve:
            print('Your input must be a number.')
            print('Native Python error message: ')
            print(ve, ve.__doc__, type(ve), sep='\n')
        except Exception as e:
            print('Please validate your entry and try again.')
            print('Native Python error message: ')
            print(e, e.__doc__, type(e), sep='\n')
# In Assignment 07 Pickling if the user entered any values that weren't integers the program would break.
# This try statement takes the same input from before, but now if an error occurs where the user
# enters a non-integer value we prompt them to only enter number, any other exceptions will prompt the user to
# validate their entry. Allowing them to try again without being kicked out of the program.
lstcustomer = [strname, intPhone]

objfile = open('CustomerContact.txt', 'ab')
pickle.dump(lstcustomer, objfile)
objfile.close()

# Use a while loop to continually run the pick.load function until there was no more data to load.
# Otherwise known as a EOFError.
with open('CustomerContact.txt', 'rb') as objfile:
    while True:
        try:
            lstcustFile = pickle.load(objfile)
            print(lstcustFile)
        except EOFError:
            break


