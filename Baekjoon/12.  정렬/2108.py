import sys
from typing import Counter

N = int(sys.stdin.readline())
numList = []

for i in range(N) :
    numList.append(int(sys.stdin.readline()))

ascNum = sorted(numList)

# 산술평균, 중앙값
avg = sum(numList) / len(numList)
median = ascNum[len(ascNum) // 2]

# 범위
Range = ascNum[-1] - ascNum[0]

# 최빈값
mode = 0
modeArr = Counter(ascNum).most_common()

if len(modeArr) > 1 :
    # 최빈값의 수가 같을 경우(두번 째 값 출력)
    if modeArr[0][1] == modeArr[1][1] :
        mode = modeArr[1][0]
    # 같지 않을 경우(첫번 째 값 출력)
    else :
        mode = modeArr[0][0]
else :
    mode = ascNum[0]


print(round(avg))
print(median)
print(mode)
print(Range)