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

game = [rock, paper, scissors]

computerIndex = random.randint(0,2)
computerChoice = game[computerIndex]

userInput = int(input("Type 0 for rock, type 1 for paper or type 2 for scissor"))


if userInput < 0 or userInput > 2:
    print("Invalid. Please select between 0, 1 and 2")
else:
    userChoice = game[userInput]
    print(f"Your Chose {userChoice}")
    print(f"Computer chose {computerChoice}")

    if userChoice == computerChoice:
        print("Its a draw")
    elif (userInput == 0 and computerIndex == 2) or (userInput == 1 and computerIndex == 0) or (userInput == 2 and computerIndex == 1):
        print("You win! 🎉")
    else:
        print("Computer wins! 😢")
