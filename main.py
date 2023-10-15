#!/usr/bin/env python
# coding: utf-8

"""
Author: Alex Casanova
Date: 9/24/2023
Intent: This file initializes Appt, Task, and Contact classes for use in my Calendar Project.
        It then creates a PyMongo Database for use with the project.
        This project is intended to showcase my ability to translate existing code into new programming languages.
"""

import pymongo

import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

'''
DB
'''

connection = pymongo.MongoClient("mongodb://localhost:27017/")

db = connection["database"]

appts = db['Appts']
tasks = db['Tasks']
contacts = db['Contacts']

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
    # Constructor Class
    def __init__(self, date, time, title, contact, description):
        self.date = date
        self.time = time
        self.title = title
        self.contact = contact
        self.description = description
        self.tasks = []

    # Setters for Date, Title, and Description
    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def set_title(self, title):
        self.title = title

    def set_contact(self, contact):
        self.contact = contact

    def set_description(self, description):
        self.description = description

    # Getters for Date, Title and Description
    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_title(self):
        return self.title

    def get_contact(self):
        return self.contact

    def get_description(self):
        return self.description

    def add_task(self, task):
        if (tasks.find({'title': task}) != None):
            self.tasks.append(task)
        else:
            print('nope')

    def get_tasks(self):
        return self.tasks

    # Creates a dictionary object to be added to the Appts database, with the appt's date, title and description
    def return_dict(self):
        return {'date': self.get_date(), 'time': self.get_time(), 'title': self.get_title(),
                'contact': self.get_contact(), 'description': self.get_description()}

    # Print Appt info to Console
    def print_appt(self):
        print("{0}, {1}: {2}\n{3}".format(self.get_date(), self.get_time(), self.get_title(), self.get_contact(),
                                          self.get_description(), self.get_tasks()))

    def create(self):
        record = self.return_dict()
        if record['title'] != "":
            if (appts.find_one(record) != None):
                return ("This record already exists!")
            if (appts.find_one(record) == None):
                appts.insert_one(record)
                return ("Record Saved!")
        else:
            return "Appointments must have a name!"

    def read(self):
        record = self.return_dict()
        if (appts.find(record) != None):
            print(appts.find_one(record))
        if (appts.find(record) == None):
            print("Not in DB!")

    def update(self, date, time, title, contact, description):
        # Save existing record as dict for look up
        record = self.return_dict()

        # Fully update record with new info
        self.set_date(date)
        self.set_time(time)
        self.set_title(title)
        self.set_contact(contact)
        self.set_description(description)

        # Generates new record to update to in DB
        new_record = self.return_dict()
        if (appts.find(new_record) != None):
            appts.update_one(record, {'$set': new_record})

        if (appts.find(record) == None):
            print("Couldn't be found!")

    def delete(self):
        record = self.return_dict()
        if (appts.find(record) != None):
            x = appts.delete_many(record)
            print(x.deleted_count, "documents deleted.")
        if (appts.find(record) == None):
            print("Couldn't be found!")


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

    # Constructor Class
    def __init__(self, title, description):
        self.title = title
        self.description = description

    # Setters for Title, and Description

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    # Getters for Title, and Description

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
        if record['title'] != "":
            if (tasks.find_one(record) != None):
                return ("This record already exists!")
            if (tasks.find_one(record) == None):
                tasks.insert_one(record)
                return ("Record Saved!")
        else:
            return "Tasks must have a name!"

    def read(self):
        record = self.return_dict()
        if (tasks.find(record) != None):
            return (tasks.find_one(record))
        if (tasks.find(record) == None):
            return ("Not in DB!")

    def update(self, title, description):
        # Save existing record as dict for look up
        record = self.return_dict()

        # Fully update record with new info
        self.set_title(title)
        self.set_description(description)

        if (tasks.find(record) != None):
            # Generates new record to update to in DB
            new_record = self.return_dict()
            if (tasks.find(new_record) != None):
                tasks.update_one(record, {'$set': new_record})
                return "Record Updated!"
        if (tasks.find(record) == None):
            print("Couldn't be found!")

    def delete(self):
        record = self.return_dict()
        if (tasks.find(record) != None):
            x = tasks.delete_many(record)
            print(x.deleted_count, "documents deleted.")
        if (tasks.find(record) == None):
            print("Couldn't be found!")


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

    # Constructor Class
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

    # return_dict(self):
    # Creates a dictionary object to be added to the Contacts database, with the contact's name, phone, address and notes.
    def return_dict(self):
        return {'name': self.get_name(), 'phone': self.get_phone(), 'address': self.get_address(),
                'notes': self.get_notes()}

    def create(self):
        record = self.return_dict()
        if record['name'] != "":
            if (contacts.find_one(record) != None):
                return ("This record already exists!")
            if (contacts.find_one(record) == None):
                contacts.insert_one(record)
                return ("Record Saved!")
        else:
            return "Contacts must have a name!"

    def read(self):
        record = self.return_dict()
        if (contacts.find(record) != None):
            print(contacts.find_one(record))
        if (contacts.find(record) == None):
            return ("Not in DB!")

    def update(self, date, time, title, description):
        # Save existing record as dict for look up
        record = self.return_dict()

        # Fully update record with new info
        self.set_date(date)
        self.set_time(time)
        self.set_title(title)
        self.set_description(description)

        if (contacts.find(record) != None):
            # Generates new record to update to in DB
            new_record = self.return_dict()
            contacts.update_one(record, {'$set': new_record})

        if (contacts.find(record) == None):
            return ("Couldn't be found!")

    def delete(self):
        record = self.return_dict()
        if (contacts.find(record) != None):
            x = contacts.delete_many(record)
            return (x.deleted_count, "documents deleted.")
        if (contacts.find(record) == None):
            return ("Couldn't be found!")


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calendar App')
        self.setFixedSize(1250, 850)
        self.initUI()
        self.show()

        self.taskListUpdate()

    def initUI(self):
        # Calendar
        self.cal = QCalendarWidget(self)
        self.cal.setGeometry(10, 10, 550, 400)
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.showDate)
        self.cal.clicked[QDate].connect(self.taskListUpdate)

        # Date Label
        self.date = QLabel(self)
        self.date.setGeometry(600, 0, 550, 40)
        self.date.setText(self.cal.selectedDate().toString('MM/dd/yyyy'))

        self.newContact = QPushButton(self)
        self.newContact.setGeometry(10, 420, 200, 40)
        self.newContact.setText("New Contact")
        self.newContact.clicked.connect(lambda: self.createNewContact())

        self.newTask = QPushButton(self)
        self.newTask.setGeometry(250, 420, 200, 40)
        self.newTask.setText("New Task")
        self.newTask.clicked.connect(lambda: self.createNewTask())

        self.taskList = QListWidget()
        self.taskList.setGeometry(600, 57, 500, 775)
        self.taskList.doubleClicked.connect(lambda: self.selectAppt())

        self.taskListUpdate()

        # Window Stuff
        vbox = QVBoxLayout()
        vbox.addWidget(self.cal)
        vbox.addWidget(self.date)
        vbox.addWidget(self.taskList)
        self.layout().addWidget(self.taskList)
        self.setLayout(vbox)

    def taskListUpdate(self):
        self.taskList.clear()
        for i in range(0, 24):
            date = self.cal.selectedDate().toString("MM/dd/yyyy")
            n = QTime(i, 0, 0)
            timecode = ":00 AM"
            if (i >= 12): timecode = ":00 PM"
            time = str(i) + timecode
            appt = appts.find_one({'date': date, 'time': time})
            if appt != None:
                self.taskList.addItem(time + " - " + appt.get('contact') + " - " + appt.get('title'))
            else:
                self.taskList.addItem(time + " - ")

    def selectAppt(self):
        date = self.cal.selectedDate().toString("MM/dd/yyyy")
        time = self.taskList.currentItem().text()[:-2]
        appt = appts.find_one({'date': date, 'time': time})
        print(appt)
        if (appt == None):
            self.w = WindowNewAppt(self.cal.selectedDate())
            self.w.setWindowTitle("New Appt: " + date + " - " + time)
            self.w.show()
        self.taskListUpdate()

    def createNewContact(self):
        self.w = WindowNewContact()
        self.w.show()
        self.taskListUpdate()

    def createNewTask(self):
        self.w = WindowNewTask()
        self.w.show()
        self.taskListUpdate()

    def showDate(self, date):
        self.date.setText(date.toString('MM/dd/yyyy'))
        self.taskListUpdate()


class WindowNewAppt(QMainWindow):
    def __init__(self, QMainWindow):

        super().__init__()
        # Window
        self.setWindowTitle("New Appointment")
        self.setFixedSize(1500, 500)

        # Labels
        self.apptNameLabel = QLabel(self)
        self.apptNameLabel.setText("Appt Name")
        self.apptNameLabel.setGeometry(10, 10, 200, 40)

        self.apptDescriptionLabel = QLabel(self)
        self.apptDescriptionLabel.setText("Description")
        self.apptDescriptionLabel.setGeometry(10, 70, 200, 40)

        # Text Boxes
        self.apptNameText = QLineEdit(self)
        self.apptNameText.setPlaceholderText("Appt Name")
        self.apptNameText.setGeometry(210, 10, 400, 40)

        self.apptDescriptionText = QTextEdit(self)
        self.apptDescriptionText.setPlaceholderText("Description")
        self.apptDescriptionText.setGeometry(210, 70, 400, 200)

        # Buttons
        self.submitButton = QPushButton(self)
        self.submitButton.setText("Submit")
        self.submitButton.setGeometry(10, 400, 200, 40)
        self.submitButton.clicked.connect(lambda: self.apptSubmitButtonClicked())

        self.submitLabel = QLabel(self)
        self.submitLabel.setText("")
        self.submitLabel.setGeometry(10, 440, 500, 40)

        self.clearButton = QPushButton(self)
        self.clearButton.setText("Clear")
        self.clearButton.setGeometry(220, 400, 200, 40)
        self.clearButton.clicked.connect(lambda: self.clearAll())

        # List of Contacts
        self.contactListLabel = QLabel(self)
        self.contactListLabel.setText("Contact")
        self.contactListLabel.setGeometry(650, 10, 300, 40)

        contactArray = list(contacts.find({}))
        self.contactList = QListWidget(self)
        for i, contact in enumerate(contactArray):
            self.contactList.insertItem(i, contactArray[i].get('name'))
        self.contactList.setGeometry(650, 50, 300, 400)

        # List of Tasks
        self.taskListLabel = QLabel(self)
        self.taskListLabel.setText("Task")
        self.taskListLabel.setGeometry(960, 10, 300, 40)

        taskArray = list(tasks.find({}))
        self.taskList = QListWidget(self)
        for i, task in enumerate(taskArray):
            self.taskList.insertItem(i, taskArray[i].get('title'))
        self.taskList.setGeometry(960, 50, 300, 400)

    def apptSubmitButtonClicked(self):
        a = self.apptNameText.text()
        b = self.apptDescriptionText.toPlainText()
        c = str(self.contactList.currentItem().text())
        date = self.windowTitle()[10:20]
        time = self.windowTitle().strip()[23:]
        appt = Appt(date, time, a, c, b)

        self.submitLabel.setText(a + ": " + appt.create())
        self.clearAll()

    def clearAll(self):
        self.apptNameText.clear()
        self.apptDescriptionText.clear()


class WindowNewContact(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window
        self.setWindowTitle("New Contact")
        self.setGeometry(0, 0, 650, 500)

        # Labels
        self.contactNameLabel = QLabel(self)
        self.contactNameLabel.setText("Name")
        self.contactNameLabel.setGeometry(10, 10, 200, 40)
        contactname = self.contactNameLabel.text()

        self.contactPhoneLabel = QLabel(self)
        self.contactPhoneLabel.setText("Phone")
        self.contactPhoneLabel.setGeometry(10, 70, 200, 40)

        self.contactAddressLabel = QLabel(self)
        self.contactAddressLabel.setText("Address")
        self.contactAddressLabel.setGeometry(10, 130, 200, 40)

        self.contactNotesLabel = QLabel(self)
        self.contactNotesLabel.setText("Notes")
        self.contactNotesLabel.setGeometry(10, 190, 200, 40)

        # Text Boxes
        self.contactFirstNameText = QLineEdit(self)
        self.contactFirstNameText.setPlaceholderText("First")
        self.contactFirstNameText.setGeometry(210, 10, 170, 40)

        self.contactLastNameText = QLineEdit(self)
        self.contactLastNameText.setPlaceholderText("Last")
        self.contactLastNameText.setGeometry(390, 10, 170, 40)

        self.contactPhoneText = QLineEdit(self)
        self.contactPhoneText.setPlaceholderText("Phone")
        self.contactPhoneText.setGeometry(210, 70, 400, 40)

        self.contactAddressText = QLineEdit(self)
        self.contactAddressText.setPlaceholderText("Address")
        self.contactAddressText.setGeometry(210, 130, 400, 40)

        self.contactNotesText = QTextEdit(self)
        self.contactNotesText.setPlaceholderText("Notes")
        self.contactNotesText.setGeometry(210, 190, 400, 200)

        # Buttons
        self.submitButton = QPushButton(self)
        self.submitButton.setText("Submit")
        self.submitButton.setGeometry(10, 400, 200, 40)
        self.submitButton.clicked.connect(lambda: self.submitButtonClicked())

        self.submitLabel = QLabel(self)
        self.submitLabel.setText("")
        self.submitLabel.setGeometry(10, 440, 500, 40)

        self.submitButton = QPushButton(self)
        self.submitButton.setText("Clear")
        self.submitButton.setGeometry(220, 400, 200, 40)
        self.submitButton.clicked.connect(lambda: self.clearAll())

    def submitButtonClicked(self):
        a = self.contactFirstNameText.text() + " " + self.contactLastNameText.text()
        b = self.contactPhoneText.text()
        c = self.contactAddressText.text()
        d = self.contactNotesText.toPlainText()
        contact = Contact(a, b, c, d)
        self.submitLabel.setText(contact.create())
        self.clearAll()

    def clearAll(self):
        self.contactFirstNameText.clear()
        self.contactLastNameText.clear()
        self.contactPhoneText.clear()
        self.contactAddressText.clear()
        self.contactNotesText.clear()


class WindowNewTask(QMainWindow):
    def __init__(self):
        super().__init__()
        # Window
        self.setWindowTitle("New Task")
        self.setFixedSize(700, 500)

        # Labels
        self.taskNameLabel = QLabel(self)
        self.taskNameLabel.setText("Task Name")
        self.taskNameLabel.setGeometry(10, 10, 200, 40)

        self.taskDescriptionLabel = QLabel(self)
        self.taskDescriptionLabel.setText("Description")
        self.taskDescriptionLabel.setGeometry(10, 70, 200, 40)

        # Text Boxes
        self.taskNameText = QLineEdit(self)
        self.taskNameText.setPlaceholderText("Task Name")
        self.taskNameText.setGeometry(210, 10, 400, 40)

        self.taskDescriptionText = QTextEdit(self)
        self.taskDescriptionText.setPlaceholderText("Description")
        self.taskDescriptionText.setGeometry(210, 70, 400, 200)

        # Buttons
        self.submitButton = QPushButton(self)
        self.submitButton.setText("Submit")
        self.submitButton.setGeometry(10, 400, 200, 40)
        self.submitButton.clicked.connect(lambda: self.taskSubmitButtonClicked())

        self.submitLabel = QLabel(self)
        self.submitLabel.setText("")
        self.submitLabel.setGeometry(10, 440, 500, 40)

        self.clearButton = QPushButton(self)
        self.clearButton.setText("Clear")
        self.clearButton.setGeometry(220, 400, 200, 40)
        self.clearButton.clicked.connect(lambda: self.clearAll())

    def taskSubmitButtonClicked(self):
        a = self.taskNameText.text()
        b = self.taskDescriptionText.toPlainText()
        task = Task(a, b)
        self.submitLabel.setText(task.create())
        self.submitLabel.setText("Record for task '" + a + "' Submitted!")
        self.clearAll()

    def clearAll(self):
        self.taskNameText.clear()
        self.taskDescriptionText.clear()


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())

