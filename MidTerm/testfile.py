import random

print("Welcome to Rock, Paper, or Scissors")

# Initialize scores
user_score = 0
computer_score = 0
winning_score = 3
options = ["rock", "paper", "scissors"]

while user_score < winning_score and computer_score < winning_score:
    user_choice = input("Enter your choice: (rock, paper, scissors)\n ").lower()
    print("You chose:", user_choice)

    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(options)
    print("Computer chose:", computer_choice)

    # Determine the Winner
    if user_choice == computer_choice:
        print("It's a draw! Try again.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display current scores
    print(f"Score - You: {user_score}, Computer: {computer_score}")

# Display final result
if user_score == winning_score:
    print("Congratulations! FRANZIIIIIIIIIIIII!")
else:
    print("Computer wins the game! Better luck next time.")
