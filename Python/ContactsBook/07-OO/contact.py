"""
The contact object definition
"""

class contact:
    """
    Individual contact
    """

    # Class variable contact count
    contact_count=0
    
    def __init__(self, contact_name, contact_phone, contact_dob):
        self.__name = contact_name
        self.__phone = contact_phone
        self.__dob = contact_dob

        self.contact_count+=1

    # Add setters/getters
    def set_name(self,contact_name):
        self.__name = contact_name

    def get_name(self):
        return self.__name
    
    def set_phone(self,contact_phone):
        self.__phone = contact_phone

    def get_phone(self):
        return self.__phone

    def set_dob(self, contact_dob):
        self.__dob = contact_dob

    def get_dob(self):
        return self.__dob
    

class contacts:
    """
    Contact collection
    """

    def __init__(self):
        self.__contacts = []

    def set_contact(self,new_contact):
        self.__contacts.append(new_contact)
    
    def get_contacts(self):
        return self.__contacts
    
    def delete_contact(self,contact_name):
        counter=0
        for contact in self.__contacts:
            if contact.get_name() == contact_name:
                print(f"Name: {contact_name}")
                print(f"Phone: {contact.get_phone()}")
                print(f"Date of Birth: {contact.get_dob()}")
                break
            counter+=1
        del self.__contacts[counter]

    def __iter__(self):
        self.idx = 1
        return self.__contacts[self.idx]
    
    def __next__(self):
        contact = self.__contacts[self.idx]
        self.idx += 1
        return contact