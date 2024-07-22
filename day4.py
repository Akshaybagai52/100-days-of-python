# Virtual coin toss
import random
print("Welcome to virtual coin toss game")
rand = random.randint(0, 1)
if rand == 0:
    print("Tail")
else:
    print("Head")



# get random value from the list 

import names 
import random

random_integer = random.randint(0, len(names.names))

print(f"{names.names[random_integer]} is going to by the meal today")
