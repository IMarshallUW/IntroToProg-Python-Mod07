# ---------------------------------------------------------------------------- #
# Title: Assignment 07 Pickling and Exception Handling with Functions
# Description: Script to act as instruction for creating a working script for
#              pickling and exception handling using funcitons.
# ChangeLog (Who,When,What):
# IMarhsall,2.26.2023,Created started script for Assignment07
# IMarhsall,2.26.2023,Added script to Assignment 07 Pickling to add parameters and exception handling
# IMarhsall,2.26.2023,Rewrote script to Assignment 07 Exception Handling to perform same tasks using functions
# ---------------------------------------------------------------------------- #

# Declare variable------------------------------------------------------------ #
strPhone = ''  # User defined string to check length prior to converting to integer
intPhone = ''  # User defined integer representing a phone number converted from strPhone
strname = ''  # User defined string representing a person's name
lstcustomer = []  # A list that acts as a collection of customer info
lstcustFile = []  # Memory load of all data in CustomerContact.txt


# Code 3: Using Functions - We are building on the code from Assignment 07 Exception Handling
#                           to run the same program but with functions instead of hard coded values. Functions split
#                           the script into smaller executable chunks which allow easier use by other programs if
#                           the script is imported over to another program.
#   See bottom of page with previous code referencing how items were split to form functions.

import pickle  # Imports code from another file

def get_name():
    while True:
        strname = str(input('Please enter a first and last name: ').strip().upper())
        if ' ' not in strname:
            print('Invalid, please ensure you are entering a first AND last name.')
        else:
            return strname
        # return identifies the data entered as a variable to be used later in another function

def get_phone():
    while True:
        strPhone = str(input('Please enter a domestic phone number with area code (numbers only): ').strip())
        if len(strPhone) != 10:
            print('Invalid phone number length. Please enter a 10 digit phone number.')
        else:
            try:
                intPhone = int(strPhone)
                return intPhone
            except ValueError as ve:
                print('Your input must be a number.')
                print('Native Python error message: ')
                print(ve, ve.__doc__, type(ve), sep='\n')
            except Exception as e:
                print('Please validate your entry and try again.')
                print('Native Python error message: ')
                print(e, e.__doc__, type(e), sep='\n')

def save_customer():
    strname = get_name()
    intPhone = get_phone()
    lstcustomer = [strname, intPhone]
    print('-----The following data was written to file-----')
    print(lstcustomer)

    objfile = open('CustomerContact.txt', 'ab')
    pickle.dump(lstcustomer, objfile)
    objfile.close()

def read_customers():
    with open('CustomerContact.txt', 'rb') as objfile:
        while True:
            try:
                lstcustFile = pickle.load(objfile)
                print(lstcustFile)
            except EOFError:
                break

# We made a menu interface to allow for easier user interface and multiple data entry.
def menu():  # User interface menu
    while True:
        choice = input('''
       Please select one of the following:
        1) Save a new customer
        2) View customers on file
        3) Exit program
        ''')
        if choice == '1':
            save_customer()
        elif choice == '2':
            read_customers()
        elif choice == '3':
            break
        else:
            print('Invalid choice, please try again.')
    print('Thank you and have a nice day.')

if __name__ == '__main__':
    menu()
    # Checks if program is being executed directly from file. If the program is being
    # imported the user can still use the functions but the menu will not open on starting.


#-------------------------------------------------------------------------------------#
# Below is code from Assignment07 Exception Handling with a break down about how the code was made into functions.
# 1st section was separated into three distinct funtions
# Retrieving the customer name became the get_name() function
'''
while True:
    strname = str(input('Please enter a first and last name: ').strip())
    if ' ' not in strname:
        print('Invalid, please ensure you are entering your first and last name.')
    else:
        break
'''
# Retrieving the customer's phone number, checks, and exception handling became the get_phone() function
'''
while True:
    strPhone = str(input('Please enter a domestic phone number with area code (numbers only): ').strip())
    if len(strPhone) != 10:
# Checks to make sure that there are 10 characters entered
# Changed to start as string and check for length first.
# Then become integer and check to see if data are numbers, since data entry didn't recognize 0 as an integer intitially
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
# In Assignment 07 Pickling is the user entered any values that weren't integers the program would break.
# This try statement takes the same input that was commented out above, but now if an error occurs where the user
# enters a non-integer value we prompt them to only enter number, any other exceptions will prompt the user to
# validate their entry. Allowing them to try again without being kicked out of the program.
'''
# Adding the data to the list, showing the data in the list and appending the memory to the file were all combined
# into the save_customer() function since it's good practice to separate user input functions from background processes.
'''
lstcustomer = [strname, intPhone]
print(lstcustomer)

# We will use pickle.dump to store the data
objfile = open('CustomerContact.txt', 'ab')
# 'ab' appends the data in the file, allowing us to add to it without overriding it while defining it as binary.
pickle.dump(lstcustomer, objfile)
objfile.close()

# To verify the data saved we will read back everything contained in it with pickle.load

# Commented out to write a code with exception handling that will load all the lines in the file instead of one
'''
# Reading all the data in the file became the read_customer() function
'''
with open('CustomerContact.txt', 'rb') as objfile:
    while True:
        try:
            lstcustFile = pickle.load(objfile)
            print(lstcustFile)
        except EOFError:
            break
# Use a while loop to continually run the pick.load function until there was no more data to load.
# Otherwise known as a EOFError.
'''