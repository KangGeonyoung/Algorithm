import copy
import sys

def N_queen(x, y, chess, preChess, queenCnt) :
    global result, N

    preChess = copy.deepcopy(chess)
    
    print(f"n_queen {x}, {y}")
    # 퀸을 체스판에 놓았기 때문에 queenCnt +1 해주기
    queenCnt += 1

    # x, y 자리의 값을 0으로 변환
    chess[x][y] = 0

    # x, y값에 해당하는 row, col의 값을 0으로 변환
    for i in range(N) :
        chess[x][i] = 0
        chess[i][y] = 0
    
    # 대각선 0으로 변환
    for i in range(N) :
        for j in range(N) :
            if (i+j) == (x+y) or abs(i-j) == abs(x-y) :
                chess[i][j] = 0

    

    # 퀸을 체스판에 다 놓았다면 경우의 수(result) 증가 시키기
    if queenCnt == N :
        result += 1
        return chess

    print(chess)

    # 다음 퀸 자리 찾는 과정
    for i in range(N) :
        for j in range(N) :
            if chess[i][j] == 1 :
                
                chess = N_queen(i, j, chess, preChess, queenCnt)
    
    if queenCnt != N :
        return preChess

    
N = int(sys.stdin.readline())
result = 0

for i in range(N) :
    for j in range(N) :
        chess = [[1 for col in range(N)] for row in range(N)]
        preChess = copy.deepcopy(chess)
        queenCnt = 0
        chess = N_queen(i, j, chess, preChess, queenCnt)

print(result)
