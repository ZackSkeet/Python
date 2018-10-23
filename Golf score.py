hole1 = input("Whats your score for hole 1?")
hole2 = input("Whats your score for hole 2?")
hole3 = input("Whats your score for hole 3?")
hole4 = input("Whats your score for hole 4?")

Total = int(hole1) + int(hole2) + int(hole3) + int(hole4)

if Total >= 11:
    print("Your score is " + str(int(hole1) + int(hole2) + int(hole3) + int(hole4)) + " you where over par")
else:
    if Total <= 11:
        print("Your score is " + str(int(hole1) + int(hole2) + int(hole3) + int(hole4)) + " you where under par")
    elif Total == 11:
        print("Your score is " + str(int(hole1) + int(hole2) + int(hole3) + int(hole4)) + " on par")