name = input("what is your name\n")

awesomelevel = 0


for char in name:
    if char.lower() in ("a","e","i","o","u"):
        awesomelevel += 1


print("Your awesome level is: " + str(awesomelevel))

print("********************************************\n\n")

