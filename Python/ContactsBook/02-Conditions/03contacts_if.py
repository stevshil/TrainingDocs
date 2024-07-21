#!/usr/bin/env python
"""
Now adding conditional checks
"""

# Let's get input from the user using input()
contact_name = input("Please enter contact name: ")

contact_phone = input("Please enter contact mobile number: ")
# Check that the phone number contains numbers only
if contact_phone.isdigit():
    # Note how the next line is indented to be a part of the if body
    print("Phone number meets requirements")
else:
    # Note the next 2 lines are part of the else condition which happens if the if condition is false
    print("Error: invalid phone number.  Numbers only.")
    exit(1) # Exit the program with a system error

contact_dob = input("Please enter contacts date of birth (YYYY-MM-DD): ")

# We will set the ID programmatically
contact_id = 1

# We can also use the following to display variables rather than concatenate
# The f before the "" means format string.
print(f"ID: {contact_id}")
print(f"Name: {contact_name}")
print(f"Mobile: {contact_phone}")
print(f"D.O.B.: {contact_dob}")