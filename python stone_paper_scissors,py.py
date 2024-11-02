import random

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

def get_user_choice():
    user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
    while user_choice not in ['stone', 'paper', 'scissors']:
        print("Invalid choice, please try again.")
        user_choice = input("Enter your choice (stone, paper, scissors): ").lower()
    return user_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Stone, Paper, Scissors!")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(user_choice, computer_choice)
        print(result)
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
