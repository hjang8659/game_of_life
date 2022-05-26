# Made by HyunDong (Daniel) Jang
# My first project
# Began 5/19/21

import random

rows = 10
cols = 10

board = []

def random_board_init():
    global board
    for i in range(rows):
        row = []
        board.append(row)
        for j in range(cols):
            # rand_bit = bool(random.getrandbits(1))
            # row.append(rand_bit)
            row.append(False)
    board[3][4] = True
    board[4][5] = True
    board[5][3] = True
    board[5][4] = True
    board[5][5] = True


def get_neighbors(i, j):
    counter = 0
    if i > 0 and j > 0 and board[i-1][j-1]:
        counter += 1
    if i > 0 and board[i-1][j]:
        counter += 1
    if i > 0 and j < cols - 1 and board[i-1][j+1]:
        counter += 1
    if j > 0 and board[i][j-1]:
        counter += 1
    if j < cols - 1 and board[i][j+1]:
        counter += 1
    if i < rows - 1 and j > 0 and board[i+1][j-1]:
        counter += 1
    if i < rows - 1 and board[i+1][j]:
        counter += 1
    if i < rows - 1 and j < cols -1 and board[i+1][j+1]:
        counter += 1
    return counter
    
def live_or_die():
    global board
    new_board = []
    for i in range(rows):
        new_row = []
        new_board.append(new_row)
        for j in range(cols):
            neigh_val = get_neighbors(i, j)
            if board[i][j]:
                if neigh_val < 2:
                    new_row.append(False)
                elif neigh_val == 2 or neigh_val == 3:
                    new_row.append(True)
                elif neigh_val > 3:
                    new_row.append(False)
                else:
                    new_row.append(True)
            else:
                if neigh_val == 3:
                    new_row.append(True)
                else:
                    new_row.append(False)
    board = new_board

def tick():
    live_or_die()
    display(board)

def display(board):
    for row in board:
        for elem in row:
            if elem:
                print("*", end = ' ')
            else:
                print("-", end = ' ')
        print()

random_board_init()
display(board)
while input("Press enter for the next generation: ") == "":
    tick()