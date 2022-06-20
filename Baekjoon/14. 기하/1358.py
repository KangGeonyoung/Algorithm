import math
import sys

W, H, X, Y, P = map(int, sys.stdin.readline().split())
playerInfo = [[0 for col in range(2)] for row in range(P)]
count = 0

for i in range(P) :
    playerX, playerY = map(int, sys.stdin.readline().split())

    if X <= playerX and playerX <= X + W :
        if Y <= playerY and playerY <= Y + H :
            count += 1
            continue
    
    radius = H / 2

    # 왼쪽 원의 방정식으로 비교
    if math.pow(playerX-X, 2) + math.pow(playerY - (Y + radius), 2) <= math.pow(radius, 2) :
        count += 1
        continue

    # 오른쪽 원의 방정식으로 비교
    if math.pow(playerX - (X + W), 2) + math.pow(playerY - (Y + radius), 2) <= math.pow(radius, 2) :
        count += 1
        continue

print(count)