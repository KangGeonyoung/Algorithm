import sys


board = [[0 for col in range(9)] for row in range(9)]

for i in range(9) :
    board[i] = list(map(int, sys.stdin.readline().split()))

board[0][5] = 1

for i in range(9) :
    print(board[i])

