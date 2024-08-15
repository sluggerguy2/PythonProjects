import random

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

choice_art = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]
player_choice = int(input('Choose "Rock"(0), "Paper"(1), or "Scissors"(2): '))
computer_choice = random.randint(0, 2)

if player_choice < 0 or player_choice > 2:
    print("Not a valid choice!")
    quit()

print(f"You chose {choices[player_choice]}")
print(choice_art[player_choice])
print(f"Computer chose: {choices[computer_choice]}")
print(choice_art[computer_choice])

if player_choice == 0 and computer_choice == 1 or player_choice == 2 and computer_choice == 1 or player_choice == 1 and computer_choice == 0:
    print("You won!")
elif player_choice == computer_choice:
    print("It's a tie!")
else:
    print("You lost!")
