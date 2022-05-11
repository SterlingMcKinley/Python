#!/usr/bin/env python3

#In this project I chose to complete an easy python challenge which is the RockPaperScissors game.
#This project has made it clear that I must review the different modules available for Python.

import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'
    
    return 'You lost!'

def is_win(player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
    if (player  == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
