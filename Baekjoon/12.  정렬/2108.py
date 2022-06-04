import math
from pyexpat import model
import sys

N = int(sys.stdin.readline())
numList = []

for i in range(N) :
    numList.append(int(sys.stdin.readline()))

newNum = sorted(numList)

avg = sum(numList) / len(numList)
median = newNum[len(newNum) // 2]

Max = max(numList)
Min = min(numList)
Range = Max - Min

modeList = [0] * N

for i in range(N) :
    if modeList.count(numList[i]) == 0 :
        modeList[i] += 1
    else :
        modeList[modeList.index(numList[i])] += 1


print(round(avg))
print(median)
print(Range)
print(modeList)
