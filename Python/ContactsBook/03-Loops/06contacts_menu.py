#!/usr/bin/env python
"""
Adding a menu to your code
"""

import re  # the regular expression module

# Initialise our chose option to a non-valid value
chose=300
# Set the contact id for the beginning of the program
contact_id=0

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
        fail=0
        for char in contact_phone:
            if not (char.isdigit() or char == "-"):
                print("Error: invalid phone number.  Numbers only.")
                contact_phone = None
                fail=1
                break
        
        if fail == 1:
            continue

        contact_dob = input("Please enter contacts date of birth (YYYY-MM-DD): ")
        # Check that the DOB matches the required format
        if not re.search(r'^\d{4,}-\d{2}-\d{2}$',contact_dob):
            print("Error: invalid DOB. YYYY-MM-DD.")
            contact_dob = None
            continue

        contact_id += 1

    elif chose == 2:
        try:
            # Runtime try to make sure we have all the data
            print(f"ID: {contact_id}")
            print(f"Name: {contact_name}")
            print(f"Mobile: {contact_phone}")
            print(f"D.O.B.: {contact_dob}")
        except Exception:
            # Loop to menu
            continue

        # Set an invalid response value to enter the loop. No do while in Python
        response="x"
        
        while ( response not in "yn" ):
            response = input("Delete this contact (y/n): ")

        if ( response == "y" ):
            contact_name=None
            contact_phone=None
            contact_dob=None
    
    elif chose == 3:
        try:
            print(f"ID: {contact_id}")
            print(f"Name: {contact_name}")
            print(f"Mobile: {contact_phone}")
            print(f"D.O.B.: {contact_dob}")
        except Exception:
            # Loop to menu
            continue

    elif chose == 4:
        break # Leave the current while loop

# Final statement before exiting
print("Thank you for using contacts")