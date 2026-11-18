import random
from enum import Enum
# First to three
playerScore = 0
computerScore = 0
while True:
    computerGuess = Enum('Hand', [('rock', 1), ('paper', 2), ('scissor', 3)])
    computerGuess = random.randint(1,3)
    print('first to three points win! | Player points: ' + str(playerScore) + ' Computer points: ' + str(computerScore) )
    guess = input("Pick rock, paper or scissor: ")
    
    if guess == 'rock' or guess == 'paper' or guess == 'scissor':
        if computerGuess == 1:
            print("Computer picks: rock")
            print("Player picks " + guess)
            if guess == 'rock':
                print("both picked rock: no point given")
            elif guess == 'paper':
                print("paper beats rock. 1 point given to player")
                playerScore += 1
            else:
                print('rock beats scissor. 1 point given to computer')
                computerScore += 1
        elif computerGuess == 2:
            print("Computer picks: paper")
            print("Player picks:" + guess)
            if guess == 'rock':
                print("paper beats rock. 1 point given to computer")
                computerScore += 1
            elif guess == 'paper':
                print("both picked paper. no point given")
            else:
                print("scissor beats paper. 1 point given to player")
                playerScore += 1
        else:
            print("Computer picks: scissor")
            print("Player picks: " + guess)
            if guess == 'rock':
                print("rock beats scissor. 1 point given to player")
                playerScore += 1 
            elif guess == 'paper':
                print("scissor beats paper. 1 point given to computer")
                computerScore += 1
            else:
                print("both picked scissor: no point given")
    else:
        print("Need to write either rock, paper or scissor")

    if(computerScore == 3):
        print("Computer beat the Player and won!")
        break
    elif playerScore == 3:
        print("Player got 3 points and beat the Computer!")
        break
