#!/usr/bin/python3.5

import itertools
import sys


def getBoard(size, alive_cons):
    return [[1 if (i, j) in alive_cons else 0
             for j in range(size)]
            for i in range(size)]

def getBoard2 (size, alive_cons):
    list1 = []
    list2 = []
    for i in range(size):
        for j in range(size):
            if (i, j) in alive_cons:
                list2.append(1)
            else:
                list2.append(0)
        list1.append(list2)
        list2 = []
    return list1

def getNeighbours(con):
    x, y = con
    neighbors = [(x + i, y + j)
                 for i in range(-1, 2)
                 for j in range(-1, 2)
                 if not i == j == 0]
    return neighbors


def calculateAlive(con, alive_cons):
    filtered = filter(lambda x: x in alive_cons, getNeighbours(con))
    counter = 0
    for aliver in filtered:
        counter = counter + 1
    return counter


def isAliveDot(con, alive_cons):
    alive_neighbors = calculateAlive(con, alive_cons)
    if (alive_neighbors == 3 or
            (alive_neighbors == 2 and con in alive_cons)):
        return True
    return False


def nextGeneration(alive_cons):
    board = itertools.chain(*map(getNeighbours, alive_cons))
    new_board = set([con
                     for con in board
                     if isAliveDot(con, alive_cons)])
    return list(new_board)

# def is_correct_con(size, con):
#     x, y = con
#     return all(0 <= coord <= size - 1 for coord in [x, y])
#
#
# def correct_cons(size, cons):
#     return filter(lambda x: is_correct_con(size, x), cons)

def printBoard(board):
    for line in board:
        print(line)
    print


def main():

    list = []
    row = 0
    column = 0
    size = int(sys.stdin.readline().strip())
    livingnode = int(sys.stdin.readline().strip())
    generation = int(sys.stdin.readline().strip())

    for i in range(livingnode * 2):

        if (i % 2 == 0):
            row = int(sys.stdin.readline().strip())
        else:
            column = int(sys.stdin.readline().strip())
            list.append((row,column))

    for _ in range(generation):
        list = nextGeneration(list)

    #printBoard(getBoard(size, list))
    print(getBoard(size, list))
    #print(getBoard2(size, list))


if __name__ == '__main__':
    main()
