# 런타임 에러(OverflowError)가 발생함
# 원인 : 0과 500 값을 넣었을 때 에러 발생
# factorial(0) = 1이라는 것을 예외처리 안해줌.
# / 연산자를 쓰면 결과가 float로 나오고 // 연산자를 쓰면 결과가 int로 나온다.
# overflow error : 정수 연산 계산 결과가 허용 범위를 초과한 것이다.
import sys

def factorial(n) :
    if n == 0 :
        return 1
    return n * factorial(n-1)

N = int(sys.stdin.readline())

factorialN = factorial(N)
zeroCnt = 0

while True :
    if factorialN % 10 == 0 :
        zeroCnt += 1
        factorialN = factorialN // 10
    else :
        break

print(zeroCnt)