#!/usr/bin/env python
"""
Adding storage to your code.
This method uses parallel lists, where the index is used across lists
"""

import re  # the regular expression module

# Initialise our chose option to a non-valid value
chose=300

# A set of parallel lists
contact_name_list=[]
contact_phone_list=[]
contact_dob_list=[]

# Contact ID will be the list position

# Let's control the program with a while loop
# This loop will exit when the user chooses the Exit option from the menu
while chose != 4:
    # Note the indentation here for the menu and actions

    # Print the menu each time round the loop, using multiline print
    print("""
    1. Add user details
    2. Delete user details
    3. Print contact
    4. Exit program

    """)

    chose = int(input("Chose> ")) # Prompt for menu option number, and convert input to integer
    # Input takes strings by default

    if chose == 1:
        # Adding user datails

        contact_name = input("Please enter contact name: ")
        if not re.search('^[a-zA-Z ]+$',contact_name):
            print("ERROR: name does not match requirements of letters and spaces")
            contact_name = None # Unset the variable
            continue # Go back to the start of the loop and show menu

        contact_phone = input("Please enter contact mobile number: ")
        # Now let's change the isdigit to allow for -
        # List comprehension to get invalid characters in phone number
        invalid_chars = [ (char.isdigit() or char == "-") for char in contact_phone ]
        if False in invalid_chars:
            print("Error: invalid phone number.  Numbers only.")
            print(f"You entered {invalid_chars}")
            contact_phone = None
            continue

        contact_dob = input("Please enter contacts date of birth (YYYY-MM-DD): ")
        # Check that the DOB matches the required format
        if not re.search(r'^\d{4,}-\d{2}-\d{2}$',contact_dob):
            print("Error: invalid DOB. YYYY-MM-DD.")
            contact_dob = None
            continue

        # Add detail to the lists
        contact_name_list.append(contact_name)
        contact_phone_list.append(contact_phone)
        contact_dob_list.append(contact_dob)

    elif chose == 2:

        for contact_id,contact_name in enumerate(contact_name_list):  # Enumerate returns the index and the value of the list
            print(f"{contact_id}: {contact_name}")

        get_id = int(input("Which contact would you like to delete: "))

        try:
            # Runtime try to make sure we have all the data
            print(f"ID: {get_id}")
            print(f"Name: {contact_name_list[get_id]}")
            print(f"Mobile: {contact_phone_list[get_id]}")
            print(f"D.O.B.: {contact_dob_list[get_id]}")
        except Exception:
            # Loop to menu
            continue

        # Set an invalid response value to enter the loop. No do while in Python
        response="x"
        
        while ( response not in "yn" ):
            response = input("Delete this contact (y/n): ")

        if ( response == "y" ):
            del contact_dob_list[get_id]
            del contact_name_list[get_id]
            del contact_phone_list[get_id]
    
    elif chose == 3:
        for contact_id,contact_name in enumerate(contact_name_list):  # Enumerate returns the index and the value of the list
            print(f"{contact_id}: {contact_name}")

        get_id = int(input("Which contact would you like to display: "))

        try:
            print(f"ID: {get_id}")
            print(f"Name: {contact_name_list[get_id]}")
            print(f"Mobile: {contact_phone_list[get_id]}")
            print(f"D.O.B.: {contact_dob_list[get_id]}")
        except Exception:
            # Loop to menu
            continue

    elif chose == 4:
        break # Leave the current while loop

# Final statement before exiting
print("Thank you for using contacts")