# 일반적인 방법으로 lcm을 구하면 계속 시간 초과가 발생했음.
# 유클리드 호제법을 사용하면 빠르게 결과 값을 구할 수 있다.
# ex) gcd(24, 18) = gcd(18, 6) = gcd(6, 0) => gcd = 6
# lcm = 24 * 18 / gcd(=6) = 72
import sys

x, y = map(int, sys.stdin.readline().split())
lcm = 0
gcd = 0

if x > y :
    Min = y
    Max = x
else :
    Min = x
    Max = y

# gcd(최대공약수) 구하는 과정
for i in range(Min, 0, -1) :
    if x % i == 0 and y % i == 0 :
        gcd = i
        break

# lcm(최소공배수) 구하는 과정
lcm = int(x * y / gcd)


print(gcd)
print(lcm)