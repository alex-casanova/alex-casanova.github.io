#!/usr/bin/env python
# coding: utf-8

# In[221]:


"""
Author: Alex Casanova
Date: 9/24/2023
Intent: This file initializes Appt, Task, and Contact classes for use in my Calendar Project.
        It then creates a PyMongo Database for use with the project.
        This project is intended to showcase my ability to translate existing code into new programming languages.
"""


# In[222]:


import pymongo


# In[452]:


'''
DB
'''

connection = pymongo.MongoClient("mongodb://localhost:27017/")

db = connection["database"]

appts = db['Appts']
tasks = db['Tasks']
contacts = db['Contacts']


# In[604]:


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
        
    add_task(self):
        Adds a task to the appointment if it exists in the Task list
        
    get_tasks(self):
        returns a list of all tasks assigned to the appointment
    
    
    DB Interface Methods:
        These moethods perform full CRUD functionality to the Appts Database:
            Create
            Read
            Update
            Delete
"""    
    
class Appt:
    #Constructor Class
    def __init__(self, date, time, title, description):
        self.date = date
        self.time = time
        self.title = title
        self.description = description
        self.tasks = []
    #Setters for Date, Title, and Description
    def set_date(self, date):
        self.date = date
    
    def set_time(self, time):
        self.time = time

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description
    
    #Getters for Date, Title and Description
    def get_date(self):
        return self.date    
    
    def get_time(self):
        return self.time

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    
    def add_task(self, task):
        if (tasks.find({'title': task}) != None):
            self.tasks.append(task)
        else:
            print('nope')
        
    def get_tasks(self):
        return self.tasks
    
     #Creates a dictionary object to be added to the Appts database, with the appt's date, title and description
    def return_dict(self):
        return {'date': self.get_date(), 'time': self.get_time(), 'title': self.get_title(), 'description': self.get_description()}
    
    
    #Print Appt info to Console
    def print_appt(self):
        print("{0}, {1}: {2}\n{3}".format(self.get_date(), self.get_time(), self.get_title(), self.get_description(), self.get_tasks()))
    
    def create(self):
        record = self.return_dict()
        if(appts.find_one(record) != None):
            print("This record already exists!")
        if(appts.find_one(record) == None):
            appts.insert_one(record)
            print("Record Saved!")
            
    def read(self):
        record = self.return_dict()
        if(appts.find(record) != None):
            print(appts.find_one(record))
        if(appts.find(record) == None):
            print("Not in DB!")
            
    def update(self, date, time, title, description):
        # Save existing record as dict for look up
        record = self.return_dict()
        
        # Fully update record with new info
        self.set_date(date)
        self.set_time(time)
        self.set_title(title)
        self.set_description(description)
        
        
        if(appts.find(record) != None):
            # Generates new record to update to in DB
            new_record = self.return_dict()
            if(appts.find(new_record) != None):
                appts.update_one(record, {'$set': new_record})
            
        if(appts.find(record) == None):
            print("Couldn't be found!")
    
    def delete(self):
        record = self.return_dict()        
        if(appts.find(record) != None):
            x = appts.delete_many(record)
            print(x.deleted_count, "documents deleted.")
        if(appts.find(record) == None):
            print("Couldn't be found!")
    


# In[605]:


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
        
    DB Interface Methods:
        These moethods perform full CRUD functionality to the Tasks Database:
            Create
            Read
            Update
            Delete
            
"""

class Task:
    
    #Constructor Class
    def __init__(self, title, description):
        self.title = title
        self.description = description

    # Setters for Title, and Description

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description
        
        
    #Getters for Title, and Description

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description
    
    # print_task(self):
    # Prints the title and description to the console. Mainly for testing purposes.
    def print_task(self):
        print("{0}: {1}".format(self.get_title(), self.get_description()))
    
    # return_dict(self):
    # Creates a dictionary object to be added to the Tasks database, with the task's title and description
    def return_dict(self):
        return {'title': self.get_title(), 'description': self.get_description()}
    
    def create(self):
        record = self.return_dict()
        if(tasks.find_one(record) != None):
            print("This record already exists!")
        if(tasks.find_one(record) == None):
            tasks.insert_one(record)
            print("Record Saved!")
            
    def read(self):
        record = self.return_dict()
        if(tasks.find(record) != None):
            print(tasks.find_one(record))
        if(tasks.find(record) == None):
            print("Not in DB!")
            
    def update(self, title, description):
        # Save existing record as dict for look up
        record = self.return_dict()
        
        # Fully update record with new info
        self.set_title(title)
        self.set_description(description)
        
        
        if(tasks.find(record) != None):
            # Generates new record to update to in DB
            new_record = self.return_dict()
            if(tasks.find(new_record) != None):
                tasks.update_one(record, {'$set': new_record})
            
        if(tasks.find(record) == None):
            print("Couldn't be found!")
    
    def delete(self):
        record = self.return_dict()        
        if(tasks.find(record) != None):
            x = tasks.delete_many(record)
            print(x.deleted_count, "documents deleted.")
        if(tasks.find(record) == None):
            print("Couldn't be found!")
    
    


# In[606]:


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
        
    DB Interface Methods:
        These moethods perform full CRUD functionality to the Contacts Database:
            Create
            Read
            Update
            Delete
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
        print("{0}: {1}: {2}, {3}".format(self.get_name(), self.get_phone(), self.get_address(), self.get_notes))
     
    #return_dict(self):
    #Creates a dictionary object to be added to the Contacts database, with the contact's name, phone, address and notes.
    def return_dict(self):
        return {'name': self.get_name(), 'phone': self.get_phone(), 'address': self.get_address(), 'notes': self.get_notes()}
    
    def create(self):
        record = self.return_dict()
        if(contacts.find_one(record) != None):
            print("This record already exists!")
        if(contacts.find_one(record) == None):
            contacts.insert_one(record)
            print("Record Saved!")
            
    def read(self):
        record = self.return_dict()
        if(contacts.find(record) != None):
            print(contacts.find_one(record))
        if(contacts.find(record) == None):
            print("Not in DB!")
            
    def update(self, date, time, title, description):
        # Save existing record as dict for look up
        record = self.return_dict()
        
        # Fully update record with new info
        self.set_date(date)
        self.set_time(time)
        self.set_title(title)
        self.set_description(description)
        
        
        if(contacts.find(record) != None):
            # Generates new record to update to in DB
            new_record = self.return_dict()
            contacts.update_one(record, {'$set': new_record})
            
        if(contacts.find(record) == None):
            print("Couldn't be found!")
    
    def delete(self):
        record = self.return_dict()        
        if(contacts.find(record) != None):
            x = contacts.delete_many(record)
            print(x.deleted_count, "documents deleted.")
        if(contacts.find(record) == None):
            print("Couldn't be found!")
    
    


# In[607]:


task_checkup = Task('Checkup', 'Perform a checkup')
task_checkup.create()
task_checkup.read()


# In[608]:


a = Appt("01/01/2004", "9:00 am", "John Smith Monthly Checkup", "John has high blood pressure, make sure to check this!")
a.create()
a.read()


# In[609]:


c = Contact('John', '800-525-5252', '123 Main St, Boston, MA 01231', 'John has high blood pressure.')
c.create()
c.read()


# In[ ]:




