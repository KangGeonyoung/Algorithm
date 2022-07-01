# 조합(combination)을 사용한 문제
# nCr = n! / ((n-r)! * r!)
from math import factorial
import sys

def combination(m, n) :
    if m == n :
        return 1
    elif m-n == 1 :
        return M
    else :
        return factorial(m) / (factorial(m-n) * factorial(n))

T = int(sys.stdin.readline())

for i in range(T) :
    N, M = map(int, sys.stdin.readline().split())

    print(int(combination(M, N)))
