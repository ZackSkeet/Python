
comp = 0

name1 = input("Enter your name: ")
name2 = input("Enter your name: ")

weight = 100 / len(name1 + name2)

for char in name1 + name2:
    if char.lower() not in ["l", "o", "v", "e", "s"]:
        comp -= weight

print("Your compatibility level is: " + str(int(comp)) + "%")


