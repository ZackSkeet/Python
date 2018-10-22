senior_citizen = 0
number_of_people = 0
carers = 2
total_cost = 0
cost_per_person = 0
spare_places =0
total_money_collected=0

#create an empty dictionary
names_money = {}
running = True

while running == True:
	senior_citizen = input("Please enter the number of senior citizens going on the trip\n")

	print("The number of Senior Citizens you have entered is " + str(senior_citizen))
#---------------------------------------------------------------------------------

	#If there is a valid number of senior citizens, that is between 10 and 36

	if ((int(senior_citizen) >= 10) and (int(senior_citizen)) < 36):
	
#---------------------------------------------------------------------------------
		#Set number of carers, if >24 then 3 carers else just 2 carers go along
		if (int(senior_citizen)) > 24:
			number_of_people = int(senior_citizen) +((int(carers)) + 1)
			print("Number of people going along including carers is " + str(number_of_people))
		else:
			number_of_people = int(senior_citizen) +(int(carers))
			print("Number of people going along including carers is " + str(number_of_people))
#---------------------------------------------------------------------------------
#Set costs for the three tiers, 12-16, 17-26, 27-39
		if ((int(number_of_people) >=12) and (int(number_of_people)) <=16): 
		
			#For 12-16 total cost is coach 150 + (people x meal 14) + (people x ticket 21)
			total_cost = 150 +(number_of_people*14.00) + (number_of_people*21.00)
			print ("Total Cost is " + "%.2f" % round(total_cost,2))
			cost_per_person = (int(total_cost)/int(senior_citizen))
			print("Cost per person is " + "%.2f" % round(cost_per_person,2))

		elif (int(number_of_people) >=17) and (int(number_of_people) <=26):
			#For 17-26 total cost is coach 190 + (people x meal 13.50) + (people x ticket 20)
			total_cost = 190 +(number_of_people*13.50) + (number_of_people*20.00)
			print ("Total Cost is " + "%.2f" % round(total_cost,2))
			cost_per_person = (int(total_cost)/int(senior_citizen))
			print("Cost per person is " + "%.2f" % round(cost_per_person,2))
		
		elif (int(number_of_people) >=27) and (int(number_of_people) <=39):
			#For 27-39 total cost is coach 225 + (people x meal 13.00) + (people x ticket 19)
			total_cost = 225 +(number_of_people*13.00) + (number_of_people*19.00)
			print ("Total Cost is " + "%.2f" % round(total_cost,2))
			cost_per_person = (int(total_cost)/int(senior_citizen))
			print("Cost per person is " + "%.2f" % round(cost_per_person,2))
		
#---------------------------------------------------------------------------------
#Work out the number of spare places		
		#for 12-16 people work out the number of spare places on the bus
		if ((int(number_of_people) >=12) and (int(number_of_people)) <=16):
			spare_places = (16 - int(number_of_people))
			print("Number of spare places = " + str(spare_places))
	
		#for 17-26 people work out the number of spare places on the bus	
		elif ((int(number_of_people) >=17) and (int(number_of_people)) <=26):
			spare_places = (26 - int(number_of_people))
			print("Number of spare places = " + str(spare_places))
		
		#for 27-39 people work out the number of spare places on the bus	
		elif ((int(number_of_people) >=27) and (int(number_of_people)) <=39):
			spare_places = (39 - int(number_of_people))
			print("Number of spare places = " + str(spare_places))
			
#---------------------------------------------------------------------------------
#ask if the spare places can be filled.

		#If there are spare places ask the user if they want to add more people and add to number_of_people
		if spare_places > 0:
			add_more_people = input ("There are " + str(spare_places) + " spare places. Do you want to add any more people? y/n\n>")
			if add_more_people.lower()=="y":
				extra_people = input ("Please enter how many people you would like to add\n>")
				while int(extra_people) > int(spare_places):
					extra_people = input ("Please enter a number between 1 and " + str(spare_places) + "\n>")
				number_of_people = int(number_of_people) + int(extra_people)
		print("The total number of people is " + str(number_of_people))
		
#----------------------------------------------------------------------------------
#Add a name to the dictionary along with the amount of money paid
		for name in range(int(number_of_people)):
			addname = input("Enter the name to add in:\n>".lower())

			#if word isn't in dictionary add it along with its meaning
			if addname not in names_money:
				amount_paid = input("How much have they paid?\n")
				names_money[addname] = amount_paid
				total_money_collected = int(total_money_collected) + int(amount_paid)
		
#--------------------------------------------------------------------------------------
# Once all the names are input break out of the while loo
		break
		
		
#--------------------------------------------------------------------------------------	
# If an invalid number of senior citizens is entered then tell the user and go back to enter a valid number
	else:
		print("Number of senior citizens must be more than 10 or less than 36")
		
		
#--------------------------------------------------------------------------------------
#Print out the list of names and amounts

print()
print()
print("You have entered the following names and amounts")
for names in names_money:
	print (names, names_money[names])
print()
print()
print("Total Money Collected is "+ str(total_money_collected))
