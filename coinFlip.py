# Coin flip 
# Head or Tails?
import random
import string
secret = random.randint(1, 100)
head = "head"
tails = "tails"
while True:
    guess = input('head or tails: ')
    if guess == head or guess == tails:
        if secret <= 50:
            print("heads!")
            if(guess == head):
                print("you guess correctly!")
                break
            else:
                print("you guess incorrectly!")
                break
        if secret > 50:
            print("Tails!")
            if(guess == tails):
                print("you guess correctly!")
                break
            else:
                print("you guess incorrectly!")
                break
    else:
        print("write head or tails: ")

