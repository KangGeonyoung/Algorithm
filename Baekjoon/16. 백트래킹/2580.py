# pypy3로 제출해야 통과됨
# row, col, 사각형 3가지 방법에 모든 숫자를 넣어서 True가 나오는지 검사 
import sys

def checkRow(y, a) :
    for i in range(9) :
        if a == board[y][i] :
            return False
    return True

def checkCol(x, a) :
    for i in range(9) :
        if a == board[i][x] :
            return False
    return True

def checkSquare(y, x, a) :
    ny = y // 3 * 3
    nx = x // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if a == board[ny + i][nx + j] :
                return False
    return True

def dfs(idx) :
    if idx == len(blank) :
        for i in range(9) :
            print(*board[i])
        exit(0)
    
    for k in range(1, 10) :
        y = blank[idx][0]
        x = blank[idx][1]
        if checkRow(y, k) and checkCol(x, k) and checkSquare(y, x, k) :
            board[y][x] = k
            dfs(idx+1)
            board[y][x] = 0


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []

for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            blank.append((i, j))


dfs(0)