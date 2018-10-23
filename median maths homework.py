homeworkmarks = [10, 6, 6, 7, 5, 0, 2, 4]
#positions         0  1  2  3  4  5  6  7

position = 0
totalmarks = 0

while position <=len(homeworkmarks)-1:
    totalmarks += homeworkmarks[position]
    position += 1
    average = str(int(totalmarks)/(len(homeworkmarks)-1))
print("The total marks are: " + str(totalmarks))
print("The total average is: " + str(average))

