# import guess.py, coinFlip.py, rockPaperScissor.py, higherOrLower.py

while True:
    print("GAMES")
    print("1. (Guess the number)")
    print("2. (Flip a coin)")
    print("3. (Rock Paper Scissor)")
    print("4. (higher or lower)")
    print("5. (hangman)")
    print("6. (black jack)")
    print("7. (tic tac toe)")
    print("8. (working progress)")
    print("9. (working progress)")
    print("10. (working progress)")
    print("11. (exist)")
    answer = input("number: ")
    if answer == "1" or answer == "2" or answer == "3" or answer == "4" or answer == "5" or answer == "6" or answer == "7" or answer == "8" or answer == "9" or answer == "10" or answer == "11":
        if answer == "1":
            import guess
        elif answer == "2":
            import coinFlip
        elif answer == "3":
            import rockPaperScissor
        elif answer == "4":
            import higherOrLower
        elif answer == "5":
            import hangman
        elif answer == "6":
            import blackJack
        elif answer == "7":
            import ticTacToe
        elif answer == "8":
            print("in working progress")
        elif answer == "9":
            print("in working progress")
        elif answer == "10":
            print("in working progress")
        elif answer == "11":
            break
    else:
        print("write a number")

