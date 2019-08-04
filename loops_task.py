
# ask the user to enter an item
item = input ('item (enter "done" when finished): ')

list_of_items = [] # the details of each bought items will be appended in this list 

while item != "done" : 
	# ask the user for the details of the item
	price = float(input ("price: "))
	quantity = int(input ("quantity: "))

	#the following dictionary will store the delaits for the current entered item
	#this dictionary will be updated for the next item
	Dict = {"item_name" : item,
			"item_price" : price,
			"item_quantity" : quantity}

	list_of_items.append(Dict) #each item will be sppended in this list with its details

	item = input ('item (enter "done" when finished): ') #if the user enter done ... it will exit this while loop

#print ("Trial 1 : Dict =", Dict)
#print ("Trial 2 : List of items =", list_of_items)


# this part of code will be excuted if the user enter "done"
print ("-----------------")
print ("receipt")
print ("-----------------")

total_price = 0 #initial value for the total price

# loop in the list of items and calculate the receipt
for bought_item in list_of_items :
	print ("%d %s %.2fKD" %(bought_item["item_quantity"] , bought_item["item_name"] , bought_item["item_price"]*bought_item["item_quantity"]))
	total_price = total_price + (bought_item["item_quantity"]*bought_item["item_price"])

print ("-----------------")
print ("total: %.2fKD" % total_price)


