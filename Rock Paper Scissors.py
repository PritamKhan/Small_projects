# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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
game_img = [rock, paper, scissors]

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors. \n"))
if user >= 3 or user < 0:
    print("You type an invalid number")
else:
    print(game_img[user])

    computer = random.randint(0,2)
    print("Computer chose:")
    print(game_img[computer])

    if  user ==  computer :
        print("it's a draw")
    elif ( user == 0 and computer == 1 ) or ( user == 1 and    computer == 2 ) or ( user == 2 and computer == 0 ):
        print("You lose")
    elif ( user == 0 and computer == 2 ) or ( user == 2 and computer == 1 ) or ( user == 1 and computer == 0 ):
        print("You win")
    

print("This repl has exited, |run again|")
