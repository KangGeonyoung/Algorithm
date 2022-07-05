# 런타임에러, 시간초과, 틀림 모두 나온 문제
# 팩토리얼에서 특정 숫자가 몇 번 곱해지는지 구하는 함수가 있음.
# 조합 공식에서 분모와 분자에서 나오는 숫자로 0이 몇 번 나오는지 구할 수 있다.
# 결과 값에서 나오는 0의 개수 = 분자에서 나오는 0의 개수 - 분모에서 나오는 0의 개수
# 2와 5의 조합으로 0이 만들어지는데 2의 횟수, 5의 횟수를 구해서 min값을 찾으면 그것이 0의 개수가 된다.

import sys

def two_cnt(n) :
    cnt = 0
    while n != 0 :
        n = n // 2
        cnt += n
    return cnt

def five_cnt(n) :
    cnt = 0
    while n != 0 :
        n = n // 5
        cnt += n
    return cnt

n, m = map(int, sys.stdin.readline().split())
result = min(two_cnt(n) - two_cnt(n-m) - two_cnt(m), five_cnt(n) - five_cnt(n-m) - five_cnt(m))

print(result)