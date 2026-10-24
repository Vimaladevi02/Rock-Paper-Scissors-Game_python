import random
print("Rock, Paper, Scissors Game")
computer = random.randint(1, 3)
print("1. Rock")
print("2. Paper")
print("3. Scissors")

user = int(input("Enter your choice (1-3): "))
if computer == 1:
    computer_choice = "Rock"
elif computer == 2:
    computer_choice = "Paper"
else:
    computer_choice = "Scissors"

print("Computer choice:", computer_choice)

if user<1 or user>3:
    print("Invalid choice!")
elif user == computer:
    print("It's a tie!")
elif user == 1 and computer == 3:
    print("You win!")
elif user == 2 and computer == 1:
    print("You win!")
elif user == 3 and computer == 2:
    print("You win!")
else:
    print("Computer wins!")
