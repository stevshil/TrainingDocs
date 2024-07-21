#!/usr/bin/env python
"""
Now adding conditional checks
"""

# We need to import a module with capabilities
import re  # the regular expression module

contact_name = input("Please enter contact name: ")
# Check the that the name contains only letters and spaces
# re.search() is the function from the imported module
if not re.search('^[a-zA-Z ]+$',contact_name):
    print("ERROR: name does not match requirements of letters and spaces")
    exit(1)

# Reg ex cheatsheet https://learnbyexample.github.io/python-regex-cheatsheet/

contact_phone = input("Please enter contact mobile number: ")
# If without else is also possible, changing the logic using not
if not contact_phone.isdigit():
    print("Error: invalid phone number.  Numbers only.")
    exit(2)

contact_dob = input("Please enter contacts date of birth (YYYY-MM-DD): ")
# Check that the DOB matches the required format
if not re.search(r'^\d{4,}-\d{2}-\d{2}$',contact_dob):
    print("Error: invalid DOB. YYYY-MM-DD.")
    exit(3)

# We will set the ID programmatically
contact_id = 1

# We can also use the following to display variables rather than concatenate
# The f before the "" means format string.
print(f"ID: {contact_id}")
print(f"Name: {contact_name}")
print(f"Mobile: {contact_phone}")
print(f"D.O.B.: {contact_dob}")