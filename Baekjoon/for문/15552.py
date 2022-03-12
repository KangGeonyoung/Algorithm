import sys

T = int(input())
result = [0] * T

for i in range(T) :
    a, b = map(int, sys.stdin.readline().split())
    result[i] = a + b

for i in range(T) :
    print(result[i])