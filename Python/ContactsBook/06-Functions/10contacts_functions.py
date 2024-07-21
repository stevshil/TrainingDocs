#!/usr/bin/env python
"""
Using functions to make code more maintainable and reuse.
"""

import re  # the regular expression module

# Initialise our chose option to a non-valid value
chose=300

# A dictionary to store our contacts
contacts={}

# Function add user
def add_user():
    # Adding user datails

    local_contacts={}

    contact_name = input("Please enter contact name: ")
    if not re.search('^[a-zA-Z ]+$',contact_name):
        print("ERROR: name does not match requirements of letters and spaces")
        contact_name = None # Unset the variable
        return False # Go back to the start of the loop and show menu

    contact_phone = input("Please enter contact mobile number: ")
    # Now let's change the isdigit to allow for -
    # List comprehension to get invalid characters in phone number
    invalid_chars = [ (char.isdigit() or char == "-") for char in contact_phone ]
    if False in invalid_chars:
        print("Error: invalid phone number.  Numbers only.")
        print(f"You entered {invalid_chars}")
        contact_phone = None
        return False

    contact_dob = input("Please enter contacts date of birth (YYYY-MM-DD): ")
    # Check that the DOB matches the required format
    if not re.search(r'^\d{4,}-\d{2}-\d{2}$',contact_dob):
        print("Error: invalid DOB. YYYY-MM-DD.")
        contact_dob = None
        return False

    local_contacts[contact_name]={"phone": contact_phone, "dob": contact_dob}

    # Return the 
    return local_contacts

def display_contacts(local_contacts,message):
    contact_list={}
    counter=0
    for contact_name in local_contacts:  # Enumerate returns the index and the value of the list
        print(f"{counter}: {contact_name}")
        contact_list[counter]=contact_name
        counter+=1

    try:
        get_option = int(input(f"Which contact would you like to {message}: "))
        get_name=contact_list[get_option]

        if get_name == "":
            return False
    except Exception:
        return False

    try:
        # Runtime try to make sure we have all the data
        print(f"Name: {get_name}")
        print(f"Mobile: {local_contacts[get_name]["phone"]}")
        print(f"D.O.B.: {local_contacts[get_name]["dob"]}")
    except Exception:
        # Loop to menu
        return False

    return get_name


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
        tmp_contacts=add_user()
        if tmp_contacts == False:
            # Skip as detail was not complete
            continue
        else:
            # Update the dictionary
            contacts.update(tmp_contacts)

    elif chose == 2:

        get_name = display_contacts(contacts,"delete")
        if get_name == False:
            continue

        # Set an invalid response value to enter the loop. No do while in Python
        response="x"
        
        while ( response not in "yn" ):
            response = input("Delete this contact (y/n): ")

        if ( response == "y" ):
            del contacts[get_name]
    
    elif chose == 3:
        get_name = display_contacts(contacts,"display")

    elif chose == 4:
        break # Leave the current while loop

# Final statement before exiting
print("Thank you for using contacts")