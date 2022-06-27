import math
import sys

def GCD(n1, n2) :
    if n2 == 0 :
        return n1
    
    return GCD(n2, n1%n2)

N = int(sys.stdin.readline())
num = list()
newNum = list()
gcd = 0
factor = list()

for i in range(N) :
    num.append(int(sys.stdin.readline()))

num = set(num)
num = list(num)

for i in range(len(num)) :
    if len(num) == 1 :
        newNum.append(num[0])
        break

    if i+1 == len(num) :
        break
    newNum.append(abs(num[i+1] - num[i]))

for i in range(len(newNum)) :
    # 값이 하나일 때
    if len(newNum) == 1 :
        gcd = newNum[0]
        break

    # indexOutOf 예방
    if i+1 == len(newNum) :
        break

    # 두 개씩 최대공약수를 찾아서 gcd에 업데이트
    gcd = GCD(newNum[i], gcd)


for i in range(2, int(math.sqrt(gcd))+1) :
    if gcd % i == 0 :
        factor.append(i)
        factor.append(int(gcd/i))
factor.append(gcd)

factor = set(factor)
factor = list(factor)
factor.sort()

for i in range(len(factor)) :
    print(factor[i], end=' ')