import random
import streamlit as st

def get_computer_choice():
    choices = ['stone', 'paper', 'scissors']
    return random.choice(choices)

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
    st.title("Stone, Paper, Scissors")

    # Let user pick their choice
    user_choice = st.selectbox("Choose your option", ['stone', 'paper', 'scissors'])

    if st.button("Play"):
        computer_choice = get_computer_choice()

        # Show the choices
        st.write(f"You chose: {user_choice}")
        st.write(f"Computer chose: {computer_choice}")

        # Determine and display the winner
        result = determine_winner(user_choice, computer_choice)
        st.write(result)

# Streamlit runs the app with this command
if __name__ == "__main__":
    play_game()
