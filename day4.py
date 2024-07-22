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





# Rock, Paper & scissor game :

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

asci_list = [rock, paper, scissors]

input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

random_int = random.randint(0,2)
if input == random_int :
    print(f"Your choice : \n {asci_list[input]} \n Computer's choice : \n {asci_list[random_int]} \n It's a draw")

elif input == 0 and random_int == 1 :
    print(f"Your choice : \n {asci_list[input]} \n Computer's choice : \n {asci_list[random_int]} \n You just won")

elif input == 0 and random_int == 2 :
    print(f"Your choice : \n {asci_list[input]} \n Computer's choice : \n {asci_list[random_int]} \n You just lost")
