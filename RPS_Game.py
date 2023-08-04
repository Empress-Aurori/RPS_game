# Rock, Paper, Scissors Game

from random import randint

# Choices that the player and computer can choose from
choices = ["rock", "paper", "scissors"]

# Conditions to be able to win/loose the game (EX: rock beats scissors)
win_conditions = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }


# Will ask the player to choose rock, paper, or scissors and return their response
def ask_player():
    while True:
        txt = input("Type one of these choices [Rock, Paper, or Scissors]: ").lower()
        if txt in choices:
            return txt
        else:
            print("INVALID RESPONSE, try again.")


# Returns a random value from the "choices" list
def ai_select():
    return choices[randint(0, 2)]


# Returns who the winner is
def get_winner(player_choice, ai_choice):
    while True:
        print("The player chose", player_choice)
        print("The computer chose", ai_choice)
        if player_choice == ai_choice:
            player_choice = ask_player()
            ai_choice = ai_select()
        elif player_choice == win_conditions[ai_choice]:
            return "the computer!"
        elif ai_choice == win_conditions[player_choice]:
            return "the player!"


# Main function for the game to run, returns the winner
def play_game():
    player_choice = ask_player()
    ai_choice = ai_select()
    return print("The winner is", get_winner(player_choice, ai_choice))


# Starts the game
play_game()
