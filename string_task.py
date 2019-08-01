# printing some welcoming sentences...
print ("Welcome!")
print ("Here.. you are going to create your oun story =D")
print ("Have a nice time...")
print(" ")
print ("Please, enter the following...")
print(" ")

# to store the inputs in variables
time = int(input ("Number: ")) # convert the input to integer regardless what is it
items = str(input("Noun: "))
name = str(input("Name: ")).title() # to capitalize only the first letter of each word
scream = str(input("Any sentence: ")).upper() # to capitalize all the letters
action = str(input("Verb: "))

# just having some spaces / lines
print ("")
print ("")

# printing the story ...
print ("It was", time, "o'clock when I heard a knock at the door.")
print ("I opened the door and there was a box full of", items, "with a note saying \"From Mr. %s\"." %(name))
print ("Just as I closed the door I heard a scream \"%s.\"." %(scream))
print ("I froze in place and all I could do was %s." %(action))