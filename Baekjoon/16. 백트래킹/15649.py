# 중복 없이 사전 순 (= 제일 앞만 정렬되면 됨)

import sys

def sequence(origin, present, M) :
    # present의 크기와 M이 같다면
    if len(present) == M :
        for i in range(len(present)) :
            print(present[i], end=" ")
        print()
    else :
        for i in range(len(origin)) :
            if origin[i] not in present :
                present.append(origin[i])
                sequence(origin, present, M)
                present.remove(origin[i])


N, M = map(int, sys.stdin.readline().split())
origin = [i+1 for i in range(N)]
present = list()

sequence(origin, present, M)