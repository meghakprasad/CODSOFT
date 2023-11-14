# Rock paper Scissors Game

import random

def get_user_choice():
    while True:
        user_choice = input("\nChoose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

def play_again():
    return input("Do you want to play again? (yes/no): ").lower() == 'yes'

def main():
    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        play_game()

        if not play_again():
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()
