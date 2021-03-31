true = 0
love = 0

name1 = input("Type the first name here: ")
name2 = input("Type the second name here: ")

name1Cap = name1.upper()
name2Cap = name2.upper()

TotalName = name1Cap + name2Cap

for element in TotalName:
    if element == "T":
        true += 1
    elif element == "R":
        true += 1
    elif element == "U":
        true += 1
    elif element == "E":
        true += 1
        love += 1
    if element == "L":
        love += 1
    elif element == "O":
        love += 1
    elif element == "V":
        love += 1

totalString = str(true) + str(love)

total = int(totalString)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos")

elif 40 < total < 50:
    print(f"Your score is {total}, you are alright together")

else:
    print(f"Your score is {total}")
