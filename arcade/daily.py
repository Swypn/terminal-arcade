# import guess.py, coinFlip.py, rockPaperScissor.py, higherOrLower.py

while True:
    print("GAMES")
    print("1. (Guess the number)")
    print("2. (Flip a coin)")
    print("3. (Rock Paper Scissor)")
    print("4. (higher or lower)")
    print("5. (exist)")
    answer = input("number: ")
    if answer == "1" or answer == "2" or answer == "3" or answer == "4" or answer == "5":
        print("choosen")
        if answer == "1":
            import guess
        elif answer == "2":
            import coinFlip
        elif answer == "3":
            import rockPaperScissor
        elif answer == "4":
            import higherOrLower
        elif answer == "5":
            break
    else:
        print("write a number")

