#!/usr/bin/env python
"""
This is a pydoc section.
There should be a pydoc section at the top of your code to explain what it does.
This is in accordance with pylinters which will check against PEP8 style coding
- https://peps.python.org/pep-0008/

This app is a basic start to creating a contacts book.
We start with variables and input/output, syntax and layout.
"""

# This a simple comment.  We will assign values to variables first

contact_id = 1
contact_name = "Steve Shillng" # This is a comment, but the line before creates and assigns a variable called contact_name
contact_phone = "555-1234"
contact_dob = "2024-01-01"
entry_hash = sin(contact_id)*cos(contact_id)

try: # We are using this to capture the error at runtime
    print("ID: " + contact_id) # This wil fail TypeError as contact_id is a number
except Exception as e: # This allows us to show what happened
    print("Error from print: "+str(e))

print("ID: " + str(contact_id)) # The str() function converts numbers to strings to concatentate with other strings
print("Name: " + contact_name) # The + symbol allows us to join strings together (concatenate)
print("Mobile: " + contact_phone)
print("D.O.B.: " + contact_dob)

# We can also use the following to display variables rather than concatenate
# The f before the "" means format string.
print(f"ID: {contact_id}") # Note automatic detection of type
print(f"Name: {contact_name}\nMobile: {contact_phone}\nD.O.B.: {contact_dob}") # \n is new line