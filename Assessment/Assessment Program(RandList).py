import random

list = []
for num in range(100):
    nums = random.randrange(1, 1000)
    list.append(nums)
print(list)

def avg(thing):
    counter = 0
    adder = 0
    for item in thing[:]:
        counter += 1
        adder += int(item)
    avg = adder / counter
    print("The average of this list is ", avg)
avg(list)
