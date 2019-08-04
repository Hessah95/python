

skills = [ "Python", "Java", "HTML", "Graphic Design", "Origami", "Crochet", "Tennis", "Bowling"]

cv = {} # an empty dictionary to be filled later

print ("Welcome to the special recruitment program, please answer the following questions:")
cv["name"] = input ("name: ")
cv["age"] = int (input ("age: "))
cv["experience"] = int (input ("how many years of experience do you have? "))
cv["skills"] = []

# printing the skills one by one:
n = 1
for item in skills :
	print ("{}- {}".format(n, item))
	n = n + 1

# asking the user to choose two skills:
value1 = input ("choose a skill from above: ")
value2 = input ("choose another skill from above: ")


def choose (val, lst,skl):
	for item in lst :
		if val == str(lst.index(item) + 1) :
			skl.append(item)
			#print ("try in function:", skl)
	return(skl)

# calling function to append the choosen skills in list in dictionary
choose(value1, skills, cv["skills"])
choose(value2, skills, cv["skills"])

#print ("try :", cv["skills"])

if ( 20 < cv["age"] < 30) :
	if cv["experience"] >= 1 :
		if ("Python" and "Java") in cv["skills"] :
			# it's required to have both python and java as skills
			print ("Congrats! you have been accepted,", cv["name"])
		else :
			print ("Sorry {}! you have not been accepted :( ,, skills does not match!".format(cv["name"]))
	else :
		print ("Sorry {}! you have not been accepted :( ,, you don't have enough years of experience!!".format(cv["name"]))
else :
	print ("Sorry {}! you have not been accepted :( ,, your age is not acceptable !!".format(cv["name"]))
