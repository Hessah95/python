# Age Calcolator ;)

from datetime import date 



def check_birthdate (year, month, day) :

	if today > In_Date :
		# the given birthdate is in the past
		return True
	elif today < In_Date :
		# the given birthdate is in the future
		return False
	


def calculate_age (year, month, day) :

	Years = today.year - In_Date.year - ( (today.month, today.day) < (In_Date.month, In_Date.day) )
	# This equation calculates the year and contains the part which ensure if we have reached the age that supposed for this year or not yet,, 
	# it compares current month and day with borm month and day and it will return 1 (True) or 0 (False)

	Months = today.month - In_Date.month
	if Months < 0 :
		Months = 12 + Months
		# In case if the current month is less than the born month

	Days = today.day - In_Date.day
	if Days < 0 :
		Days = 31 + Days
		# In case if the current day is less than the born day,, 
		# This code may gives not accuret result cuz it just determin the case of 31 days/month 

	# printing the result ...
	print ("You are", Years, "years,", Months, "months, and", Days, "days")



today = date.today() # to store the current date

# asking the user to enter his date of birth...
year = int(input ("Enter year of birth: "))
month = int(input ("Enter month of birth: "))
day = int(input ("Enter day of birth: "))

In_Date = date(year, month, day) # to store the intered date

if check_birthdate (year, month, day) == True :
	# the given birthdate is in the past
	calculate_age (year, month, day)
elif check_birthdate (year, month, day) == False :
	# the given birthdate is in the future
	print ("Hay!! You came from the future O_O'")
else :
	print ("It's imposiple !!! ofcourse this is not your birthday -_- \nYour age is less than a day =P")