# readline()을 사용하면서 뒤에 붙는 개행문자(\n)를 없애려면
# 뒤에 strip()을 추가로 붙여주면 된다.
import sys

N, M = map(int, sys.stdin.readline().split())
noListen = list()
noSee = set()

matchCnt = 0
matchList = []

for i in range(N) :
    noListen.append(sys.stdin.readline().strip())

for i in range(M) :
    noSee.add(sys.stdin.readline().strip())

for i in range(N) :
    if noListen[i] in noSee :
        matchCnt += 1
        matchList.append(noListen[i])

matchList.sort()

print(matchCnt)
for i in range(matchCnt) :
    print(matchList[i])