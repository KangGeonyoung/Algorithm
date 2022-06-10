# s = {} 이렇게 쓰면 dict 선언으로 인식된다.
# 따라서 s = set() 이렇게 선언해줘야 한다.
import sys

N, M = map(int, sys.stdin.readline().split())
wordSet = set()
checkList = list()

for i in range(N) :
    wordSet.add(sys.stdin.readline())

for i in range(M) :
    checkList.append(sys.stdin.readline())

matchCnt = 0

for i in range(M) :
    if checkList[i] in wordSet :
        matchCnt += 1

print(matchCnt)