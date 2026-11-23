import random

cardSet = {
    "Ace":      11,
    "2":        2,
    "3":        3,
    "4":        4,
    "5":        5,
    "6":        6,
    "7":        7,
    "8":        8,
    "9":        9,
    "10":       10,
    "Jack":     10,
    "Queen":    10,
    "King":     10}
playerHands = []
dealerHands = []
playerHands.append(random.choice(list(cardSet.keys())))
dealerHands.append(random.choice(list(cardSet.keys())))
playerHands.append(random.choice(list(cardSet.keys())))
dealerHands.append(random.choice(list(cardSet.keys())))
playerScore = 0
dealerScore = 0
hasPlayerLost = False
hasDealerLost = False

while True:
    playerScore = 0
    for key in playerHands:
        playerScore += cardSet.get(key)

    if playerScore > 21:
        hasPlayerLost = True
        break

    print("players hand: " + str(playerHands))
    print("dealers hand: " + str(dealerHands))
    guess = input("(h)it or (s)tand: ")
    if guess == "h" or guess == "s" or guess == "stand" or guess == "hit":
        if guess == "h" or guess == "hit":
            print("player hit")
            playerHands.append(random.choice(list(cardSet.keys())))
        else:
            print("player stand")
            break
    else:
        print("need to press h or s")

if not hasPlayerLost:
    while True:
        dealerScore = 0
    
        for key in dealerHands:
            dealerScore += cardSet.get(key)
    
        if dealerScore > 21:
            hasDealerLost = True
            break
        elif dealerScore >= 17:
            break
        else:
            dealerHands.append(random.choice(list(cardSet.keys())))
else:
    for key in dealerHands:
        dealerScore += cardSet.get(key)

print("players hand: " + str(playerHands))
print("dealer hand: " + str(dealerHands))

print(str(playerScore))
print(str(dealerScore))
if hasPlayerLost:
    print("house wins")
elif hasDealerLost:
    print("player wins")
elif playerScore > dealerScore:
    print("player wins")
elif playerScore < dealerScore:
    print("house wins")
else:
    print("draw, the house wins!")
