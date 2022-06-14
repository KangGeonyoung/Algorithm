import math
import sys

coordinate = [0] * 3
result = []

i = 0
while True :
    coordinate[0], coordinate[1], coordinate[2] = map(int, sys.stdin.readline().split())
    if coordinate[0] == 0 or coordinate[1] == 0 or coordinate[2] == 0 :
        break
    coordinate.sort()

    if math.pow(coordinate[0], 2) + math.pow(coordinate[1], 2) == math.pow(coordinate[2], 2) :
        result.append("right")
    else :
        result.append("wrong")

for i in range(len(result)) :
    print(result[i])