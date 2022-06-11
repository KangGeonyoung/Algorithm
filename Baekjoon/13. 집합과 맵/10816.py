# dictionary 또한 set 계열이기 때문에 검색 속도가 매우 빠른 편이다.
import sys

dic = dict()

N = int(sys.stdin.readline())
cardList = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
checkList = list(map(int, sys.stdin.readline().split()))
checkSet = set(checkList)

for i in range(M) :
    dic[checkList[i]] = 0

for i in range(N) :
    if cardList[i] in checkSet :
        dic[cardList[i]] += 1

for i in range(M) :
    print(dic[checkList[i]], end=' ')
