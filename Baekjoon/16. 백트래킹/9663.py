import sys

def N_queen(x, y) :
    global queenCnt, result, chess

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

            # if chess[i][j] == (x+y) or chess[i][j] == abs(x-y) :
            #     chess[i][j] = 0

    # 퀸을 체스판에 다 놓았다면 경우의 수(result) 증가 시키기
    if queenCnt == N :
        result += 1
        queenCnt = 0
        return 0

    # 다음 퀸 자리 찾는 과정
    for i in range(N) :
        for j in range(N) :
            if chess[i][j] == 1 :
                N_queen(i, j)


N = int(sys.stdin.readline())
result = 0
queenCnt = 0
chess = [[1 for col in range(N)] for row in range(N)]

for i in range(N) :
    for j in range(N) :
            N_queen(i, j)

print(result)
