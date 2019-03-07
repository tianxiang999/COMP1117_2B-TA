#!/usr/bin/python3.5

import sys


def getNeighbours(con):
    x, y = con
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not i == j == 0:
                neighbors.append((x + i, y + j))
    return neighbors


def calculateAlive(con, alive_cons):
    neighbors = getNeighbours(con)
    counter = 0
    for k in neighbors:
        if k in alive_cons:
            counter = counter + 1

    return counter


def isAliveDot(con, alive_cons):
    alive_neighbors = calculateAlive(con, alive_cons)
    if (alive_neighbors == 3 or
            (alive_neighbors == 2 and con in alive_cons)):
        return True
    return False

def nextGeneration(alive_cons):

    board = []
    aliveset = []

    for i in range(5):
        for j in range(5):
            if alive_cons[i][j] == 1:
                aliveset.append((i,j))
                board.append (getNeighbours((i,j)))

    new_board = []
    for k in range(len(board)):
        for con in board[k]:
            if isAliveDot(con, aliveset):
                new_board.append(con)

    conf = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    for con in new_board:
        x, y = con
        conf[x][y] = 1

    return conf

def main():

    cur_conf = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    row = 0
    column = 0
    size = int(sys.stdin.readline().strip())
    generation = int(sys.stdin.readline().strip())

    row = sys.stdin.readline().strip()
    while row != "t":
        column = sys.stdin.readline().strip()
        cur_conf[int(row)-1][int(column)-1] = 1
        row = sys.stdin.readline().strip()


    for _ in range(generation):
        cur_conf = nextGeneration(cur_conf)

    print(cur_conf)



if __name__ == '__main__':
    main()
