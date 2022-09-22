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
import random
value = input("what do you choose ? Type 0 for Rock , 1 for Paper, 2 for Scissors.")
val = int(value)
comp_val = random.randint(0,2)
print("Your choice\n")
if(val == 0):
  print(rock)
elif val == 1:
  print(paper)
elif val==2:
  print(scissors)
else:
  print("Invalid choice")
if(comp_val == 0):
  print(rock)
elif comp_val == 1:
  print(paper)
else :
  print(scissors)
print(comp_val)
if ((val==1 and comp_val==2) or 
    (val==2 and comp_val==0) or
    (val==0 and comp_val==1)):
  print("You lost")
elif val == comp_val:
  print("It's a draw")
else:
  print("You won")

