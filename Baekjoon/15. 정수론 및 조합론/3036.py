# 기약 분수로 만드는 방법
# : GCD(최대공약수)를 구해서 나눠주면 약분이 되어 기약 분수가 된다.
import sys

def GCD(n1, n2) :
    if n2 == 0 :
        return n1
    
    return GCD(n2, n1 % n2)

N = int(sys.stdin.readline())
ling = list(map(int, sys.stdin.readline().split()))

for i in range(1, N) :
    gcd = GCD(ling[0], ling[i])

    print(f"{int(ling[0] / gcd)}/{int(ling[i] / gcd)}")
