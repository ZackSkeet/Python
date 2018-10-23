leet = { "a" : "4",
         "b" : "13",
         "c" : "(",
         "d" : "[)",
         "e" : "3",
         "g" : "6",
         "l" : "1",
         "o" : "0",
         "s" : "5",
         "t" : "7",
         "w" : "\/\/"}
textin = input("Enter text for translation: ")
textout = ""
for char in textin:
    if char in leet:
        textout += leet[char]

    else:
        textout += char
print(textout)