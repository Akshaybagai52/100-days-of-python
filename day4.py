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

random_integer = random.randint(0, len(names.names) - 1)

print(f"{names.names[random_integer]} is going to by the meal today")



# Hidden Treasure
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
pos = 0
ind = int(position[1:2]) - 1

if position[0:1]=="A":
  pos = 0
elif position[0:1]=="B":
  pos = 1
else:
  pos = 2

print(pos, ind)
map[pos][ind] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
