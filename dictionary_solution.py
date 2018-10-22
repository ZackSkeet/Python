#the dictionary contains sms abbreviations and their meanings

dictionary = {
	"LOL"	: "laughing out loud",
	"JK"	: "just kidding",
	"ROFL"	: "rolling on the floor laughing"}
	
#print main menu
print(" SMS to English translator")
print("		t = translate")
print("		a = add word")
print("		d = delete word")
print("		p = print")
print("		q = quit")
print("==========================")

#begin by making an empty variable for the choice
choice =""

#keep asking for the choice while choice is empty or equals q
while len(choice) <= 0 or choice != "q":
	
		#get user's choice and take first letter and make it lower case
		choice = input("Make your choice\n")[0].lower()
		
	#--------------------------------------------------------------------
		#if choice is anything beginning with t
		if choice == "t":
			
			#get the sms abbreviation from user
			message = input("Enter the sms you want to translate:\n")
			
			#make an empty variable for the translation
			msgOut = ""
			
			#break up each letter of the input message and 
			#turn it into upper case
			for word in message.upper():
				#if the letter is in the dictionary then
				#translate it and add it to the output translation
				if word in dictionary:
					msgOut += dictionary[word] + " "
				#otherwise just add the word to the output without translation
				else:
					msgOut +=word.lower() + " "
					
			#print the translate test
			print("This means : " + msgOut)
	#--------------------------------------------------------------------		
		#otherwise, if user's choice is anything beginning with a
		elif choice == "a":
			
			#ask user to enter the word
			addWord = input("Enter the word to add in:\n").upper()
			#if word isn't in dictionary ad it along with its meaning
			if addWord not in dictionary:
				meaning = input("What does this mean?\n")
				dictionary[addWord] = meaning
			#otherwise print an error message
			else:
				print ("Word already in dictionary\n")
	#--------------------------------------------------------------------			
		#otherwise, if user's choice is anything beginning with d
		elif choice == "d":
			
			#ask which word to remove from the dictionary
			delWord = input("Enter the word to delete:\n").upper()
			#if word is in the dictionary then delete it
			if delWord in dictionary:
				del dictionary[delWord]
			#otherwise print an error message
			else:
				print("Word is not in dictionary\n")
	#--------------------------------------------------------------------			
		#otherwise, if user's choice is anything beginning with p
		elif choice == "p":
			#print the dictionary
			print(dictionary) 


#textIn ="Hello this is a message"
#for word in textIn.split():
#	print(word)
