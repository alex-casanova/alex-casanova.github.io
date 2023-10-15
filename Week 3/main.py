#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
Author: Alex Casanova
Date: 9/24/2023
Intent: This file inititates Appt, Task, and Contact classes for use in my Calendar Project.
        It then creates a PyMongo Database for use with the project.
        This project is intended to showcase my ability to translate existing code into new programming languages.
"""


# In[1]:


import pymongo


# In[2]:


""" 
Appt Class
    Methods:
    __init____(self, date, title, description):
        Creates instance of object, with Date, Title and Description
    Get / Set for the folowing fields:
        Date - The date an Appointment is scheduled for
            ie. 09/20/2023
        Title - A name for the appointment
            ie. "Monthly Check-up"
        Description - A description for the appointment
            ie. "Contact requests Dr. Jones"
    print_appt(self):
        Prints the date, title and description to the console. Mainly for testing purposes.
    return_dict(self):
        Creates a dictionary object to be added to the Appts database, with the appt's date, title and description
"""    
    
class Appt:
    #Constructor Class
    def __init__(self, date, title, description):
        self.date = date
        self.title = title
        self.description = description
    #Setters for Date, Title, and Description
    def set_date(self, date):
        self.date = date

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description
    
    #Getters for Date, Title and Description
    def get_date(self):
        return self.date

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    
    #Print Appt info to Console
    def print_appt(self):
        print("{0}: {1}: {2}, {3}".format(self.get_date(), self.get_title(), self.get_description()))
    
    #Creates a dictionary object to be added to the Appts database, with the appt's date, title and description
    def return_dict(self):
        return {'date': self.get_date(), 'title': self.get_title(), 'description': self.get_description()}


# In[ ]:


"""
Task Class
    Methods:
        __init____(self, date, title, description):
            Creates instance of object, with Date, Title and Description
    Get / Set for the folowing fields:
        Date - The date a task is scheduled for
            ie. 09/20/2023
        Title - A name for the task
            ie. "Check Blood Pressure"
        Description - A description for the appointment
            ie. "Don't forget your stethoscope!"
    print_task(self):
        Prints the date, title and description to the console. Mainly for testing purposes.
    return_dict(self):
        Creates a dictionary object to be added to the Tasks database, with the task's date, title and description
"""

class Task:
    
    #Constructor Class
    def __init__(self, date, title, description):
        self.date = date
        self.title = title
        self.description = description

    # Setters for Date, Title, and Description
    def set_date(self, date):
        self.date = date

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description
        
        
    #Getters for Date, Title, and Description
    def get_date(self):
        return self.date

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    
    # print_task(self):
    # Prints the date, title and description to the console. Mainly for testing purposes.
    def print_task(self):
        print("{0}: {1}: {2}, {3}".format(self.get_date(), self.get_title(), self.get_description()))
    
    # return_dict(self):
    # Creates a dictionary object to be added to the Tasks database, with the task's date, title and description
    def return_dict(self):
        return {'date': self.get_date(), 'title': self.get_title(), 'description': self.get_description()}


# In[15]:


""" 
Conact Class
# Methods:
    __init____(self, name, phone, address, notes):
        Creates instance of object, with Name, Phone, Address, and Notes
    Get / Set for the folowing fields:
        Name - The Contact's name
            ie. "John Smith"
        Phone - The Contact's phone number
            ie. 800-555-1212
        Address - The Contact's address
            ie. "123 Main St, Boston, MA 01231"
    print_contact(self):
        Prints the name, phone, address and notes to the console. Mainly for testing purposes.
    return_dict(self):
        Creates a dictionary object to be added to the Contacts database, with the contact's name, phone, address and notes.
"""

class Contact:
    
    #Constructor Class
    def __init__(self, name, phone, address, notes):
        self.name = name
        self.phone = phone
        self.address = address
        self.notes = notes
    # Setters for Name, Phone, Address, and Notes
    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_address(self, address):
        self.address = address
    
    def set_notes(self, notes):
        self.notes = self.notes + notes

    # Getters for Name, Phone, Address, and Notes
    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address
    
    def get_notes(self):
        return self.notes

    
    # print_contact(self):
    # Prints the name, phone, address and notes to the console. Mainly for testing purposes.
    def print_contact(self):
        print("{0}: {1}: {2}, {3}. {4}".format(self.get_name(), self.get_phone(), self.get_address(), self.get_notes))
     
    #return_dict(self):
    #Creates a dictionary object to be added to the Contacts database, with the contact's name, phone, address and notes.
    def return_dict(self):
        return {'name': self.get_name(), 'phone': self.get_phone(), 'address': self.get_address(), 'notes': self.get_notes}
    


# In[16]:


"""
DB Class
    Instantiates a connection to MongoClient client
    Points to the database, including tables for Appts, Tasks and Contacts.
"""

class DB:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["database"]
    appts = db["Appts"]
    tasks = db["Tasks"]
    contacts = db["Contacts"]

