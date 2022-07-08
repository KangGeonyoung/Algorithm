# 같은 수가 중복으로 들어가도 됨
# 수열은 사전 순

import sys

def sequence(origin, present, M) :
    # present의 크기와 M이 같다면
    if len(present) == M :
        for i in range(len(present)) :
            print(present[i], end=" ")
        print()
    else :
        for i in range(len(origin)) :
            present.append(origin[i])
            sequence(origin, present, M)
            present.pop()


N, M = map(int, sys.stdin.readline().split())
origin = [i+1 for i in range(N)]
present = list()

sequence(origin, present, M)