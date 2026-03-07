import random

board = [[" "]*3 for _ in range(3)]

def print_board():
    for row in board:
        print(row)

for turn in range(9):

    if turn % 2 == 0:
        print("Computer Turn")
        while True:
            r = random.randint(0,2)
            c = random.randint(0,2)
            if board[r][c] == " ":
                board[r][c] = "O"
                break
    else:
        print("User Turn")
        r = int(input("Row (0-2): "))
        c = int(input("Col (0-2): "))
        if board[r][c] == " ":
            board[r][c] = "X"

    print_board()