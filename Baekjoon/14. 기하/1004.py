# 시작점과 도착점이 원 안에 존재하는지 확인하는 문제이다.
# 만약 두 점이 같은 원 속에 있을 경우에는 count를 하지 않는다.

import math
import sys

T = int(sys.stdin.readline().strip())

for i in range(T) :
    matchCnt = 0
    startX, startY, endX, endY = map(int, sys.stdin.readline().split())
    planet = int(sys.stdin.readline().strip())
    planetInfo = [[0 for col in range(3)] for row in range(planet)]

    for j in range(planet) :
        planetInfo[j][0], planetInfo[j][1], planetInfo[j][2] = map(int, sys.stdin.readline().split())
    
    for k in range(planet) :
        count = 0
        if math.pow(startX-planetInfo[k][0], 2) + math.pow(startY-planetInfo[k][1], 2) < math.pow(planetInfo[k][2], 2) :
            count += 1
        
        if math.pow(endX-planetInfo[k][0], 2) + math.pow(endY-planetInfo[k][1], 2) < math.pow(planetInfo[k][2], 2) :
            count += 1
        
        if count != 2 :
            matchCnt += count
    
    print(matchCnt)

