# list는 in을 사용하여 원소를 하나씩 전부 비교해가며 찾는 반면,
# set은 Hash를 사용하기 때문에 list보다 더 짧은 시간 내에 찾을 수 있다.
# 따라서 순서와 상관없이 검색하는 거라면 Set을 사용하는게 훨씬 시간이 짧게 나온다.
# 1 MB = 1000000 byte
import sys

N = int(sys.stdin.readline())
cardSet = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
checkList = list(map(int, sys.stdin.readline().split()))

for i in range(M) :
    if checkList[i] in cardSet :
        print(1, end=" ")
    else :
        print(0, end=" ")