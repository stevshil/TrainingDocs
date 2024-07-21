#!/usr/bin/env python
"""
Adding storage to your code.
Moving from parallel lists to dictionaries
"""

import re  # the regular expression module

# Initialise our chose option to a non-valid value
chose=300

# A dictionary to store our contacts
contacts={}

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
        # if contact_name not in contacts: # Check if contact exists
        #     contacts={contact_name: {"phone": contact_phone, "dob": contact_dob}}
        #     # Note we have a dictionary within a dictionary
        # else: # Edit the contact if the name does exist
        contacts[contact_name]={"phone": contact_phone, "dob": contact_dob}

    elif chose == 2:

        contact_list={}
        counter=0
        for contact_name in contacts:  # Enumerate returns the index and the value of the list
            print(f"{counter}: {contact_name}")
            contact_list[counter]=contact_name
            counter+=1

        try:
            get_option = int(input("Which contact would you like to delete: "))
            get_name=contact_list[get_option]
        except Exception:
            continue

        try:
            # Runtime try to make sure we have all the data
            print(f"Name: {get_name}")
            print(f"Mobile: {contacts[get_name]["phone"]}")
            print(f"D.O.B.: {contacts[get_name]["dob"]}")
        except Exception:
            # Loop to menu
            continue

        # Set an invalid response value to enter the loop. No do while in Python
        response="x"
        
        while ( response not in "yn" ):
            response = input("Delete this contact (y/n): ")

        if ( response == "y" ):
            del contacts[get_name]
    
    elif chose == 3:
        contact_list={}
        counter=0
        for contact_name in contacts:  # Enumerate returns the index and the value of the list
            print(f"{counter}: {contact_name}")
            contact_list[counter]=contact_name
            counter+=1

        try:
            get_option = int(input("Which contact would you like to print: "))
            get_name=contact_list[get_option]
        except Exception:
            continue

        try:
            # Runtime try to make sure we have all the data
            print(f"Name: {get_name}")
            print(f"Mobile: {contacts[get_name]["phone"]}")
            print(f"D.O.B.: {contacts[get_name]["dob"]}")
        except Exception:
            # Loop to menu
            continue

    elif chose == 4:
        break # Leave the current while loop

# Final statement before exiting
print("Thank you for using contacts")