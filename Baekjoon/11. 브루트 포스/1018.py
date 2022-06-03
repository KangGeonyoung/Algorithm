N, M = map(int, input().split())
Bcnt = 0
Wcnt = 0
Min = 1000

board = [0] * N
for i in range(N) :
    board[i] = list(input())

for i in range(N - 7) :
    for j in range(M - 7) :
        Bcnt = 0
        Wcnt = 0
        for a in range(i, i + 8) :
            for b in range(j, j + 8) :
                # 짝수일 때
                if (a + b) % 2 == 0 :
                    if board[a][b] == 'B' :
                        Wcnt += 1
                    else :
                        Bcnt += 1
                # 홀수일 때
                else :
                    if board[a][b] == 'B' :
                        Bcnt += 1
                    else :
                        Wcnt += 1
        if Min > Wcnt :
            Min = Wcnt
        if Min > Bcnt :
            Min = Bcnt

print(Min)
