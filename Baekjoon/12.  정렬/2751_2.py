# 빠른 입출력 함수를 사용하면 통과 됨
import sys

N = int(sys.stdin.readline())
num = []

for i in range(N) :
    num.append(int(sys.stdin.readline()))

num.sort(reverse = False)

for i in range(N) :
    print(num[i])