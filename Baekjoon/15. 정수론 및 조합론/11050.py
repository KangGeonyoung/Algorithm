# 이항계수 정의
# (n k) = n! / k!*(n-k)!  범위 : (0 <= k <= n)
import sys

N, K = map(int, sys.stdin.readline().split())
NF, KF, NKF = 1, 1, 1

for i in range(1, N+1) :
    NF *= i

for i in range(1, K+1) :
    KF *= i

for i in range(1, N-K+1) :
    NKF *= i

print(int(NF / (KF*NKF)))