import random
score = 0
prevousNumber = random.randint(1, 100)
while True:
    currentNumber = random.randint(1, 100)
    print("your score: " + str(score) + " | higher or lower then " + str(prevousNumber))
    guess = input("Guess: ")
    print("higher or lower then " + str(prevousNumber))
    if guess == "higher" or guess == "lower":
        if currentNumber > prevousNumber:
            print("higher")
            if guess == "higher":
                print("correct. 1 point given")
                score += 1
            elif guess == "lower":
                print("lost. Total score: " + str(score))
                break
        elif currentNumber < prevousNumber:
            print("lower")
            if guess == "higher":
                print("lost. Total score:" + str(score))
                break
            elif guess == "lower":
                print("correct. 1 point given")
                score += 1
        else:
            print("tie. guess again")
    else:
        print("write higher or lower!")

    prevousNumber = currentNumber
        
