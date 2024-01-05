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
#take users choice:
import random

user_choice = int(input("What do you choose Type 0 for Rock, 1 for paper , 2 for scissors \n"))
computer_choice = random.randint(0,2)
print(f"Computer choice {computer_choice}")

if user_choice == 0 and computer_choice ==2:
    print("You Win!")
    print(rock)
elif user_choice == 2 and computer_choice ==0:
    print("You Loose!")
    print(rock)
elif user_choice == 0 and computer_choice ==1:
    print("You Loose")
    print(paper)
elif user_choice == 1 and computer_choice == 0:
    print("you win!")
    print(paper)
elif user_choice == 2 and computer_choice == 1:
    print("you win!")
    print(scissors)
elif user_choice == 1 and computer_choice == 2:
    print("you loose!")
    print(scissors)

else:
    print("You draw!")    
