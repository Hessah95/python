#importing libraries:

import sys		# to be used for exit() method
from time import *		# to be used for sleep() method
from datetime import *
#####################################################

class Employee :
	#attributes for Employee class with the initial values
	name = ""
	age = 0
	salary = 0
	employement_date = 0

	def __init__ (self, name, age, salary, employement_date, **kwargs):
		self.name = name
		self.age = age
		self.salary = salary
		self.employement_date = employement_date
		for attribut, value in kwargs.items():
			setattr (self, attribute, value)

	def get_working_years(self):
		today = datetime.now()
		return today.year-self.employement_date

	def __str__ (self):
		return "Employee(name="+self.name+", age="+str(self.age)+", salary="+str(self.salary)+", working years: "+str(self.get_working_years())+")"


#######################################################

class Manager :
	#attributes for Manager class with the initial values
	name = ""
	age = 0
	salary = 0
	employment_date = 0
	bonus_percentage = 0

	def __init__ (self, name, age, salary, employement_date, bonus_percentage, **kwargs):
		self.name = name
		self.age = age
		self.salary = salary
		self.employement_date = employement_date
		self.bonus_percentage = bonus_percentage
		for attribut, value in kwargs.items():
			setattr (self, attribute, value)

	def get_working_years(self):
		today = datetime.now()
		return today.year-self.employement_date

	def get_bonus (self):
		return self.bonus_percentage*self.salary

	def __str__ (self):
		return "Manager(name: "+self.name+", age: "+str(self.age)+", salary: "+str(self.salary)+", working years: "+str(self.get_working_years())+", bonus: "+str(self.get_bonus())+")"

#################################################################
#E = Employee("Fatmah", 31, 850, 2017)
#M = Manager("Khaled", 38, 1750, 2006, .5)

employee_list = [] # an empty list for employees to be listed later (when the user choose option #3)
manager_list = []  # an empty list for the managers to be listed later (when the user choose option #4)

print ("   Welcome to HR Pro 2019")
#time.sleep(1) #delay for 1 second
while True: #to keep looping until the user choose opthin #5 (exit())
	print ("   Choose an action to do:")
	print ("       1. show employees")
	print ("       2. show managers")
	print ("       3. add an employee")
	print ("       4. add a manager")
	print ("       5. exit")
	print ("")
	#time.sleep(2) #delay for 2 seconds
	choice = input("what would you like to do? ") # ask the user to enter the choice # ... this # will consider as string

	if choice == "1" :
		print ("-----------------")
		print ("Employees")
		for item in employee_list :
			print (item) 
		#print ("")
		print ("-----------------")
		print ("")
		#time.sleep(2) # delay for 2 seconds

	elif choice == "2" :
		print ("-----------------")
		print ("Managers")
		for item in manager_list:
			print (item) 
		#print ("")
		print ("-----------------")
		print ("")
		#time.sleep(2) #delay for 2 seconds

	elif choice == "3" :
		print ("-----------------")
		#asking the HR employee to enter the details about the normal employee
		name = input ("name: ")
		age = int(input ("age: "))
		salary = int(input ("salary: "))
		employement_date = int(input ("employement year: "))

		#creating an object for the class Employee
		employee = Employee(name, age, salary, employement_date)

		#appending all the new datas to employye_list which has been created before
		employee_list.append(employee)

		print ("Employee added succesfully")
		#print ("")
		print ("-----------------")
		print ("")
		#time.sleep(2) #delay for 2 seconds

	elif choice == "4" :
		print ("-----------------")
		#asking the HR employee to enter the details about the manager
		name = input ("name: ")
		age = int(input ("age: "))
		salary = int(input ("salary: "))
		employement_date = int(input ("employement year: "))
		bonus_percentage = float(input ("bonus percentage: "))
		
		#creating an object for the class Manager
		manager = Manager(name, age, salary, employement_date, bonus_percentage)

		#appending all the new datas to manager list which has been created before
		manager_list.append(manager)

		print ("Employee added succesfully")
		#print ("")
		print ("-----------------")
		print ("")
		#time.sleep(2) #delay for 2 seconds

	elif choice == "5" :
		sys.exit() #to exit the program