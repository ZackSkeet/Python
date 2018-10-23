#Import the module for creating random numbers
import random

print("Hello and welcome to my game where you have to keep rolling the dice till you win. When you win my application will be displayed.")
#Check if the user wants to keep playing or quit
play = input("Please press y and the enter key to begin")


#Check if they want to keep playing
while play.lower() == 'y':
    #generate an integer between 0,2
    fate = random.randint(0,1)

    if fate == 0:

        print("You lose try again")
        print("Press y to play again or n to quit")
        #They lost so they can choose not to play again
        play = input("Do you want to try again? [y/n]")

    else:

    #print my application
        print("Hello again! Well done for winning! My name is Zack Skeet and I think I'd be perfect as a Digital Leader")
        print("because I have experience teaching the Kennedy kids how to code scratch as I taught them for 2 terms with my")
        print("friend Robert lacy, we also taught them how to use and code makey makeys along with how to build and code")
        print("Lego Mindstorms. I also have experience teaching younger kids how to play football along with planning")
        print("leading the sessions. Overall I love computers and coding along with learning new things and teaching ")
        print("others about them. I have good communication skills along with very good problem solving skills. I believe")
        print("I would be an excellent addition to the team as I have plenty of ideas to help get more people interested")
        print("in doing computer science at both a GCSE level and at an IB level. Thank you for your time!")

    #Ask if they want to try and double their score
        play = input("To quit the program press n and the enter key again")
