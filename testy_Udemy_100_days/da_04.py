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
game_images = [rock, paper, scissors]
choice = int(input("What will you choose? Select 0 for ROCK, 1 for PAPER or 2 for SCISSORS: "))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)

pc_choice = random.randint(0, 2)
if pc_choice == 0:
    print("PC chose:")
    print(rock)
elif pc_choice == 1:
    print("PC chose:")
    print(paper)
else:
    print("PC chose:")
    print(scissors)

if choice == pc_choice:
    print("It's a draw!")
elif choice == 0 and pc_choice == 2:
    print("You win!")
elif pc_choice == 0 and choice == 2:
    print("You lose!")
elif choice == 1 and pc_choice == 2:
    print("You lose!")
elif choice == 2 and pc_choice == 0:
    print("You lose!")
elif choice == 0 and pc_choice == 1:
    print("You lose!")

else:
    print("You selected an INVALID NUMBER. You can't play! PC wins by default!")