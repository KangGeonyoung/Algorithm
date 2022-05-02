N = int(input())

def fiveFirst(N) :
    fiveKg = 0
    threeKg = 0
    # 5로 나눌 수 있다면
    if N >= 5 :
        fiveKg = N // 5
        N = N % 5

        if N >= 3 :
            threeKg = N // 3
            N = N % 3
            if N > 0 :
                fiveKg = -1
                threeKg = -1
        else :
            threeKg = -1
    # 5 미만의 수라면
    else :
        # 3으로 나눌 수 있다면
        if N >= 3 :
            fiveKg = 0
            threeKg = N // 3
            N = N % 3
            if N > 0 :
                fiveKg = -1
                threeKg = -1
        else :
            fiveKg = -1
            threeKg = -1

    if fiveKg == -1 or threeKg == -1 :
        return -1
    else :
        return fiveKg + threeKg

def threeFirst(N) :
    fiveKg = 0
    threeKg = 0
    # 3으로 나눌 수 있다면
    if N >= 3 :
        threeKg = N // 3
        N = N % 3
        if N > 0 :
            threeKg = -1
            fiveKg = -1

    if fiveKg == -1 or threeKg == -1 :
        return -1
    else :
        return fiveKg + threeKg

print(fiveFirst(N))
print(threeFirst(N))

if fiveFirst(N) > 0 and threeFirst(N) > 0 :
    print(min(fiveFirst(N), threeFirst(N)))

if fiveFirst(N) == -1 and threeFirst(N) == -1 :
    print(-1)

if fiveFirst(N) == -1 and threeFirst(N) > 0 :
    print(threeFirst(N))

if fiveFirst(N) > 0 and threeFirst(N) == -1 :
    print(fiveFirst(N))
