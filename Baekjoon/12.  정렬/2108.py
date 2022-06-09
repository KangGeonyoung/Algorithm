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
# Counter 클래스를 이용하면 매우 편리하다.
# Counter(변수) => 변수 속에서 등장하는 매개들의 개수를 세어 dictionary로 나타내어 return 한다.
# Counter(변수).most_common() => 위와 비슷하지만 추가적으로 데이터의 개수가 많은 순으로 정렬된 dictionary를 return 한다.

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