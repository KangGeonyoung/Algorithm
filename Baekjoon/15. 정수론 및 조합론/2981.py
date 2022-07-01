# N = M * k + R (k는 몫)
# 위 공식을 통해서 K[1]-k[0]이 N[1]-N[0]의 약수란 사실을 알게 됨
# 따라서 입력 받은 input값을 N[i+1]-N[i]로 바꿔준다.
# 새로 만들어진 input 값들을 두 개씩 GCD 함수에 넣어서 최종적인 최대 공약수를 찾아준다.
# 찾은 최대 공약수의 약수를 찾아주면 끝. (약수는 1을 제외하므로 이 점은 주의)

# 사용한 반례
# 3 36 36 36 / 4 1 5 7 11

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

# input 입력 받는 코드
for i in range(N) :
    num.append(int(sys.stdin.readline()))

# input 중복 제거 및 정렬
num = set(num)
num = list(num)

for i in range(len(num)) :
    # 값이 하나일 때
    if len(num) == 1 :
        newNum.append(num[0])
        break

    # indexOutOf 에러 예방
    if i+1 == len(num) :
        break

    # 절댓값을 이용
    newNum.append(abs(num[i+1] - num[i]))


for i in range(len(newNum)) :
    # 값이 하나일 때
    if len(newNum) == 1 :
        gcd = newNum[0]
        break

    # indexOutOf 에러 예방
    if i+1 == len(newNum) :
        break

    # 두 개씩 최대공약수를 찾아서 gcd에 업데이트
    gcd = GCD(newNum[i], gcd)

# 약수 찾는 코드
for i in range(2, int(math.sqrt(gcd))+1) :
    if gcd % i == 0 :
        factor.append(i)
        factor.append(int(gcd/i))
factor.append(gcd)

# 중복 없애고 정렬하는 코드
factor = set(factor)
factor = list(factor)
factor.sort()

# 결과 값 출력
for i in range(len(factor)) :
    print(factor[i], end=' ')