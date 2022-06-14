# 최대 넓이 - 최소 넓이
# 1번과 2번, 3번과 4번을 한쌍으로 생각하자
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

# 직사각형 밭 넓이에서 비어있는 밭 넓이
minRow = 501
minCol = 501
for i in range(6) :
    if fieldInfo[i][0] == 1 or fieldInfo[i][0] == 2 :
        if fieldInfo[i][1] < minRow :
            minRow = fieldInfo[i][1]
    else :
        if fieldInfo[i][1] < minCol :
            minCol = fieldInfo[i][1]
minArea = minRow * minCol

# 참외밭 넓이
resultArea = maxArea - minArea

# 주어진 밭에서 자라는 참외의 수
orientalMelonNum = resultArea * orientalMelon
print(orientalMelonNum)