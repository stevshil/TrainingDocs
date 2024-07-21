#!/usr/bin/env python
"""
Let's now use input from the user rather than assign directly
"""

# Let's get input from the user using input()
contact_name = input("Please enter contact name: ")
contact_phone = input("Please enter contact mobile number: ")
contact_dob = input("Please enter contacts date of birth (YYYY-MM-DD): ")

# We will set the ID programmatically
contact_id = 1

# We can also use the following to display variables rather than concatenate
# The f before the "" means format string.
print(f"ID: {contact_id}")
print(f"Name: {contact_name}")
print(f"Mobile: {contact_phone}")
print(f"D.O.B.: {contact_dob}")

# Add a second contact
contact_id += 1 # Short cut for writing  contact_id = contact_id + 1

contact_name = input("Please enter contact name: ")
contact_phone = input("Please enter contact mobile number: ")
contact_dob = input("Please enter contacts date of birth (YYYY-MM-DD): ")

print(f"ID: {contact_id}")
print(f"Name: {contact_name}")
print(f"Mobile: {contact_phone}")
print(f"D.O.B.: {contact_dob}")