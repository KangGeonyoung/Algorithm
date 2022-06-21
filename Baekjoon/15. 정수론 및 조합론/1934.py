# 유클리드 호제법을 이용해서 GCD(최대 공약수)를 구하면 LCM(최소 공배수)을 쉽게 구할 수 있다.
import sys

def GCD(A, B) :
    if B == 0 :
        return A
    
    return GCD(B, A % B)


T = int(sys.stdin.readline())

for i in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    LCM = A * B / GCD(A, B)
    print(int(LCM))