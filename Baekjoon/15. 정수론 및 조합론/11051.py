# DP(Dynamic Programming)을 이용한 문제
# 파스칼의 삼각형을 사용
# [1001][1001] 배열을 만들어서 row와 col이 0이 되는 부분은 모두 1 값을 넣어줌
# 규칙에 따라서 값을 배열에 대입해주고 dp를 이용해 값을 찾음
# 여기서는 dp[N-K][K]로 했을 때 정답이 나왔음
import sys

N, K = map(int, sys.stdin.readline().split())
dp = [[0 for col in range(1001)] for row in range(1001)]

for i in range(N+1) :
    for j in range(K+1) :
        if j == 0 :
            dp[i][j] = 1
        elif i == 0 :
            dp[i][j] = 1
        else :
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 10007

print(dp[N-K][K])
