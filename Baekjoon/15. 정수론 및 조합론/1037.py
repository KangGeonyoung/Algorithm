# N에 대한 약수들 중에서 첫 번째 값(1)과 마지막 값(N)을 제외한 나머지 값 중에서
# min과 max를 곱하면 N이 나오게 된다.
import sys

factorNum = int(sys.stdin.readline().strip())
factor = list(map(int, sys.stdin.readline().strip().split()))
result = 0

if len(factor) == 1 :
    result = factor[0] * factor[0]
else :
    result = min(factor) * max(factor)

print(result)