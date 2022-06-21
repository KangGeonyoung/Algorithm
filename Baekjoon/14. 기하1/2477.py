# 1번과 2번, 3번과 4번을 한쌍으로 생각하자
# 시계 방향인지 반시계 방향인지 모두 확인한다.
# 유일하게 다른 방향으로 가는 부분을 최대 넓이(직사각형)에서 빼준다. 
import sys

orientalMelon = int(sys.stdin.readline().strip())
fieldInfo = [[0 for col in range(2)] for row in range(6)]

# 육각형이기 때문에 6개의 정보가 제공됨
for i in range(6) :
    fieldInfo[i][0], fieldInfo[i][1] = map(int, sys.stdin.readline().split())

# 직사각형 밭 넓이
maxRow = 0
maxCol = 0
for i in range(6) :
    if fieldInfo[i][0] == 1 or fieldInfo[i][0] == 2 :
        if fieldInfo[i][1] > maxRow :
            maxRow = fieldInfo[i][1]
    else :
        if fieldInfo[i][1] > maxCol :
            maxCol = fieldInfo[i][1]
maxArea = maxRow * maxCol

# 시계 방향인지 반시계 방향인지 찾는 과정
clockDirection = dict()
nonClockDirection = dict()
direction = []

clockDirection[1] = 3
clockDirection[2] = 4
clockDirection[3] = 2
clockDirection[4] = 1

nonClockDirection[1] = 4
nonClockDirection[2] = 3
nonClockDirection[3] = 1
nonClockDirection[4] = 2

# 방향 6개 찾기
for i in range(5) :
    if clockDirection[fieldInfo[i][0]] == fieldInfo[i+1][0] :
        direction.append("clock")
    else :
        direction.append("nonClock")

# 5번 인덱스 ->  0번 인덱스 방향은 outOfIndexError 때문에 따로 체크
if clockDirection[fieldInfo[5][0]] == fieldInfo[0][0] :
        direction.append("clock")
else :
        direction.append("nonClock")

# 방향 중에서 유일하게 다른 방향을 찾는 과정
voidIdx = direction.index(min(direction, key=direction.count))

# 찾은 다른 방향이 맨 마지막 방향일 경우
if voidIdx == 5 :
    voidArea = fieldInfo[voidIdx][1] * fieldInfo[0][1]
else :
    voidArea = fieldInfo[voidIdx][1] * fieldInfo[voidIdx+1][1]

# 참외밭 넓이
resultArea = maxArea - voidArea

# 주어진 밭에서 자라는 참외의 수
orientalMelonNum = resultArea * orientalMelon
print(orientalMelonNum)