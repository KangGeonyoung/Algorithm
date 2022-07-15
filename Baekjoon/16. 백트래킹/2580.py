import sys

def sudoku(i, j) :
    row = list()
    col = list()
    square = list()

    for m in range(9) :
        if board[i][m]

    return 

board = [[0 for col in range(9)] for row in range(9)]

# input 입력 받는 코드
for i in range(9) :
    board[i] = list(map(int, sys.stdin.readline().split()))

# 0을 발견하면 sudoku 함수 실행
for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            sudoku(i, j)

