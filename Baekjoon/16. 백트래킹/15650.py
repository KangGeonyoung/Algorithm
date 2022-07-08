# 중복 없이 오름차순 (= 수열 자체가 오름차순이어야 함.)

import sys

def sequence(origin, present, M) :
    check = ""

    # present의 크기와 M이 같다면
    if len(present) == M :
        for i in range(len(present)) :
            if i+1 < len(present) :
                if present[i] > present[i+1] :
                    break
            check += f"{present[i]} "
        if len(check) == M * 2 :
            result.append(check)
    else :
        for i in range(len(origin)) :
            if origin[i] not in present :
                present.append(origin[i])
                sequence(origin, present, M)
                present.remove(origin[i])


N, M = map(int, sys.stdin.readline().split())
origin = [i+1 for i in range(N)]
present = list()
result = list()

sequence(origin, present, M)

for i in range(len(result)) :
    print(result[i])