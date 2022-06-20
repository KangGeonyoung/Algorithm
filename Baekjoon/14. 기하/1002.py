# 틀렸던 이유 : 절대값을 고려하지 못함.
# 내접을 구하는 코드를 쓰는 과정에서 r1 - r2가 마이너스 값이 나올 수 있다는 것을 고려하지 못함.
# 케이스마다 다 구해야 하기 때문에 꽤 복잡한 문제인듯. 
import math

T = int(input())

for i in range(T) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    # 두 점이 같은 좌표일 때
    if x1 == x2 and y1 == y2 :
        # 두 원이 서로 완전히 겹칠 때
        if r1 == r2 :
            print(-1)
        # 원 안에 원이 겹치지 않고 포함되어 있을 때
        else :
            print(0)
    # 서로 다른 좌표일 때
    else :
        # 두 원이 완전히 떨어져 있을 때, 원 안에 원이 겹치지 않고 포함되어 있을 때
        if r1 + r2 < dist or r1 > dist + r2 or r2 > dist + r1 :
            print(0)
        # 내접 or 외접
        elif abs(r1 - r2) == dist or r1 + r2 == dist :
            print(1)
        # 그 외에는 두 원이 서로 겹칠 때
        else :
            print(2)