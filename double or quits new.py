#open a file
fi = open("score.txt", "r")

#get the data
data = fi.readline()

#close the file
fi.close()

highscore = int(data.split(":")[0])

highname = data.split(":")[1]


print("current highscore is" + str(highscore) + "held by" + highname)

#Import the module for creating random numbers
import random

#Check if the user wants to keep playing or quit
play = 'y'

#Start the user at one
score = 1

#Check if they want to keep playing
while play.lower() == 'y':
    #generate an integer between 0,3
    fate = random.randint(0,3)

    if fate == 0:
        #they lose and score is set to 0
        print("You lose!!!")
        score = 0
        #They lost so they can choose not to play again
        play = 'n'
    else:

        # display their new score (score*2)
        score *= 2

        # print their new score
        print("Your score is now:" + str(score))

        # Ask if they want to try and double their score
        play = input("Do you want to try to double your score? [y/n]")

if score > highscore:
    newname = input("HIGH SCORE! Enter your name: ")
    fi = open("score.txt", "w")
    fi.write(str(score) + ":" + newname)
    fi.close()

