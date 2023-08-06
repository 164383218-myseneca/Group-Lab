import random

<<<<<<< HEAD
def get_user_choice():
    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        print("Invalid choice. Please try again.")

=======
>>>>>>> main
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

<<<<<<< HEAD
def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == "yes"

=======
>>>>>>> main
def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
<<<<<<< HEAD
    
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(options)

        print(f"You chose {user_choice}. Computer chose {computer_choice}.")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Your Score: {user_score}, Computer Score: {computer_score}")

        if not play_again():
            print("Thanks for playing. Goodbye!")
            break
=======

    user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
    computer_choice = random.choice(options)

    print(f"You chose {user_choice}. Computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1

    print(f"Your Score: {user_score}, Computer Score: {computer_score}")
>>>>>>> main

if __name__ == "__main__":
    rock_paper_scissors()
