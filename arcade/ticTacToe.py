width = 3
height = 3
grid = []
gridLine = []
background = "."
for i in range(width):
    gridLine.append(background)
for i in range(height):
    grid.append(list(gridLine))
is1Occupied = False
is2Occupied = False
is3Occupied = False
is4Occupied = False
is5Occupied = False
is6Occupied = False
is7Occupied = False
is8Occupied = False
is9Occupied = False
grid[0][0] = "1"
grid[0][1] = "2"
grid[0][2] = "3"
grid[1][0] = "4"
grid[1][1] = "5"
grid[1][2] = "6"
grid[2][0] = "7"
grid[2][1] = "8"
grid[2][2] = "9"

while True:
    print("tic tac toe")
    for i in range(len(grid)):
        print(grid[i])
    print("player 1")
    guess = input("number: ")
    if guess == "1" and not is1Occupied:
        grid[0][0] = "x"
        is1Occupied = True
    elif guess == "2" and not is2Occupied:
        grid[0][1] = "x"
        is2Occupied = True
    elif guess == "3" and not is3Occupied:
        grid[0][2] = "x"
        is3Occupied = True
    elif guess == "4" and not is4Occupied:
        grid[1][0] = "x"
        is4Occupied = True
    elif guess == "5" and not is5Occupied:
        grid[1][1] = "x"
        is5Occupied = True
    elif guess == "6" and not is6Occupied:
        grid[1][2] = "x"
        is6Occupied = True
    elif guess == "7" and not is7Occupied:
        grid[2][0] = "x"
        is7Occupied = True
    elif guess == "8" and not is8Occupied:
        grid[2][1] = "x"
        is8Occupied = True
    elif guess == "9" and not is9Occupied:
        grid[2][2] = "x"
        is9Occupied = True
    else:
        print("incorrect input, next player turn instead")
    for i in range(len(grid)):
        print(grid[i])
    
    print("player 2")
    guess = input("number: ")
    if guess == "1" and not is1Occupied:
        grid[0][0] = "o"
        is1Occupied = True
    elif guess == "2" and not is2Occupied:
        grid[0][1] = "o"
        is2Occupied = True
    elif guess == "3" and not is3Occupied:
        grid[0][2] = "o"
        is3Occupied = True
    elif guess == "4" and not is4Occupied:
        grid[1][0] = "o"
        is4Occupied = True
    elif guess == "5" and not is5Occupied:
        grid[1][1] = "o"
        is5Occupied = True
    elif guess == "6" and not is6Occupied:
        grid[1][2] = "o"
        is6Occupied = True
    elif guess == "7" and not is7Occupied:
        grid[2][0] = "o"
        is7Occupied = True
    elif guess == "8" and not is8Occupied:
        grid[2][1] = "o"
        is8Occupied = True
    elif guess == "9" and not is9Occupied:
        grid[2][2] = "o"
        is9Occupied = True
    else:
        print("incorrect input, next player turn instead")


