# 같은 수가 중복으로 들어가도 됨
# 수열은 비 내림차순

import sys

def sequence(origin, present, M) :
    # present의 크기와 M이 같다면(= 조건에 맞는 수열을 찾은 경우)
    if len(present) == M :
        for i in range(len(present)) :
            print(present[i], end=" ")
        print()
    else :
        for i in range(len(origin)) :
            # present에 요소 개수가 0개일 경우 Max를 0으로 지정, 그 외에는 max 찾아서 지정
            if len(present) > 0 :
                Max = max(present)
            else :
                Max = 0
            
            # 현재 present의 max 값보다 크거나 같아야 present에 들어올 수 있음
            if origin[i] >= Max :
                present.append(origin[i])
                sequence(origin, present, M)
                present.pop()


N, M = map(int, sys.stdin.readline().split())
origin = [i+1 for i in range(N)]
present = list()

sequence(origin, present, M)