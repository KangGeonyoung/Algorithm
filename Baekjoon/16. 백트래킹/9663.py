import copy
import sys

def promissing(x) :
    for i in range(x) :
        # 퀸을 놓을 수 없는 조건
        # 조건 1 : 같은 col에 있을 때 
        # 조건 2 : row 차이 = col 차이라면 같은 대각선 상에 위치하는 것
        if board[x] == board[i] or abs(board[x]-board[i]) == abs(x-i) :
            return 0
    return 1

def nQueen(row) :
    global result


    # row 깊이가 N까지 갔다면 퀸을 모두 다 놓은 것임
    if row == N :
        result += 1
        return
    else :
        for i in range(N) :
            board[row] = i
            if promissing(row) :
                nQueen(row + 1)

    
N = int(sys.stdin.readline())
result = 0
board = [0] * N

nQueen(0)
print(result)