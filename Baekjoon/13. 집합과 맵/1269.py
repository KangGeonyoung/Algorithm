import sys

aCnt, bCnt = map(int, sys.stdin.readline().split())

aList = list(map(int, sys.stdin.readline().split()))
aSet = set(aList)

bList = list(map(int, sys.stdin.readline().split()))
bSet = set(bList)

matchCnt = 0

for i in range(aCnt) :
    if aList[i] not in bSet :
        matchCnt += 1

for i in range(bCnt) :
    if bList[i] not in aSet :
        matchCnt += 1

print(matchCnt)
