#################################################################################
# Author: Obed Amissah
The Game of NIM
# Purpose: Practice breaking a larger problem down into smaller "mental chunks"using functions Aand Gain practice using loops and modulus (%)

import math                                                                                 #this imports a math library
import random                                                                               #this imports a random library


def computer_choice(state):                                                                 # this defines the function computer_move
    """this make the computer choose a random number between 1-4 when it plays"""
    move = state % 5
    if move < 1 or move>4:
        move = random.randint(1,4)                                                          #this enables the computer to make a random choice
    return move


def play():
    """this begins the game and uses input from the player and randomly generated values from the computer"""

    player = 1                                                                              #this sets the initial player to 1
    move = 0                                                                                #this sets the initial move to 0
    state = int(raw_input("Enter a number that is 15 or greater: "))
    while state < 15:                                                                       #this while loops asks the user for input and will continue doing so until correct input is entered.
        state = int(raw_input("Enter a number that is 15 or greater: "))                    #this assign state to a number that is entered by the player

    print("The number of objects is " + str(state))                                         #This shows the current state #this prints the number that the user selected
    while state > 0:
        if player % 2 == 1:                                                                 # it shows that if player is odd then it is human's turn to play.
            print("Human turn")
        else:                                                                               #it shows that if player is even then it is the computer's turn to play.
            print("computer turn")

        if player % 2 == 1:
            move = int(raw_input("What is your move?,enter number between 1-4: "))          #This asks the player to input an integer and move
            while move >4 or move < 1:
                move = int(raw_input("What is your move?,enter number between 1-4: "))      #This asks the player to input an integer and move
        else:
            move = computer_choice(state)
            print("Computer chose " + str(move))

        state = state - move                                                                #this updates the state when a move is made
        print("The number of objects is now," + str(state))                                 #This shows the current state
        if state < 1:                                                                       #This checks the status and prints the winner
            if player % 2 == 1:
                print("Human Player wins!")
            else:
                print("Computer wins!")
        else:
            player = player + 1                                                             #this ensures that there the players alternate between computer and the user.


def main():                                                                                 #this function defines the main function
    play()                                                                                  #this calls the play function in the main function
    print("Game over")                                                                      #this prints game over to signal the end of the game


main()                                                                                      #this calls the main function