#!usr/bin/python

import sys
from datetime import datetime

def new_contact():
    phonebook = []
    file = open("phonebook.txt", "a")

    firstName = raw_input("Enter First Name: ")
    lastName = raw_input("Enter Last Name: ")
    age = raw_input("Enter Age: ")
    phoneNumber = raw_input("Enter Phone Number: ")

    phonebook.append(firstName)
    phonebook.append(lastName)
    phonebook.append(age)
    phonebook.append(phoneNumber)
    print phonebook
    
    file.write(str(phonebook[0]) + ",")
    file.write(str(phonebook[1]) + ",")
    file.write(str(phonebook[2]) + ",")
    file.write(str(phonebook[3]) + "\n")
    
    #Close the file handle
    file.close()


def read_contact():
    file = open("phonebook.txt", "r")
    lines = file.readlines()
    file.close()
    
    #print lines
	#print len(lines)
	
    phonebook_read = []
    for line in lines:
		#use split function to seperate the values in each line
		#split_fields = line.splitlines()
		entry = line.rstrip().split(",")
		print "------------------------------------"
		print "First Name: %s" %entry[0]
		print "Last Name: %s" %entry[1]
		print "Phone Number: %s" %entry[3]

def search_contact():
	file = open("phonebook.txt", "r")
	lines = file.readlines()
	file.close()
	print "Search contacts for more information"
	search_first_name = raw_input("Enter the first name:")
	
	phonebook_read = []
	for line in lines:
		#use split function to seperate the values in each line
		#remove the new line character at the end of the line
		entry = line.rstrip().split(",")
		if (search_first_name == entry[0]):
			print "Search Results"
			print "------------------------------------"
			print "First Name: %s" %entry[0]
			print "Last Name: %s" %entry[1]
			print "Age: %s" %entry[2]
			print "Phone Number: %s" %entry[3]
		else: continue
			#print "Contact %s not found !!!" %search_first_name

def menu():

	application_exit = False

	#Define the Menu below
	#Add new options as you learn new ways to sort the database
	print "---------------------------"
	print "       Menu Options        "
	print "---------------------------"
	print "1. Add a New Entry to your Contacts"
	print "2. Print all the entries in your Contacts"
	print "3. Search Contacts"
	print "4. Delete a Contact"
	print "5. Find Duplicate Contacts"
	print "6. Sort Contacts"
	print "7. Quit Contacts"
    
	while(application_exit == False):
		
		#User enter the option from the Menu Option
		menu_option = raw_input("\nEnter your option: ")


		if (menu_option == "1"):
			new_contact()
		elif (menu_option == "2"):
			read_contact()
		elif (menu_option == "3"):
			search_contact()
		elif (menu_option == "7"):
			application_exit = True
		else:
			print "Error: Please enter a valid option"

	exit(0)

#call main routine
menu()







