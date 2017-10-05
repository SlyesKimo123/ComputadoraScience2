# Luke Chase
# Assessment Practice Code

### STRING PRACTICE (Immutable)
import turtle

def remove_all(substr,theStr):
    new = theStr.replace(substr, "")
    return new

print(remove_all("r", "broskraiafsr"))
# ---

string = "        the thing was a pool          "
print(string.find("t"))
print(string.count("e"))
print(string.strip())
# print("BRO" + string.ljust(1000) + "BRO")
print(string)
# ---

food = "pizza pie"
print(food[2:3])
print()
for letters in food:
    print(letters.upper())
print()
print(food.index("i"))
# ---
### LIST PRACTICE (Mutable)
myList = []
myList.append("76")
myList.append("92.3")
myList.append("hello")

print(myList)
# ---

numList = [3, 2, 34, 6, 10, 4]
for nums in numList:
    if nums % 2 == 0:
        newList = numList.append(nums)
print(newList)
# ---
### FILE PRACTICE
file = open('labdata.txt', "w")
readfile = open('labdata.txt', "r")
#data = "Things to add"
#newfile = file.write(data)
#print(newfile)
# ---

file = open("mysterypicture.txt", "r")
t = turtle.Turtle()
screen = turtle.Screen()
for lines in file:
    item = lines.split()
    if item[0] == "UP":
        t.up()
    else:
        if item[0] == "DOWN":
            t.down()
        else:
            t.goto(int(item[0]), int(item[1]))

file.close()
# ---
labfile = open("labdata.txt,", "r")
numbers = labfile.readline()
for digits in numbers:
    print(letters)
    words = labfile.readline()
