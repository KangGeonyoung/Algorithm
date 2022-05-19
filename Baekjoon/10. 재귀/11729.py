def hanoiTop(L1, L2, L3) :
    global Max, count, N, k

    # L1과 L2 중 하나라도 길이가 2 이상이라면
    if len(L1) > 1 or len(L2) > 1 :
        if len(L1) < len(L2) :
            L1.append(max(L1, L2).pop())
            k += 1
        elif len(L1) > len(L2) :
            L2.append(max(L1, L2).pop())
            k += 1

    if L3[-1] < Max :
        if L1[-1] == Max :
            L2.append(L3.pop())
            k += 1
            L3.append(L1.pop())
            k += 1
        if L2[-1] == Max :
            L1.append(L3.pop())
            k += 1
            L3.append(L2.pop())
            k += 1
    else :
        L3.append(max(L1, L2).pop())
        k += 1
    
    Max = L3[-1] - 1
    count += 1

    if count != N :
        hanoiTop(L1, L2, L3)


N = int(input())
L1 = []
L2 = []
L3 = []

for i in range(N, 0, -1) :
    L1.append(i)

# 초기 세팅
Max = max(L1)
count = 0
k = 0

# N이 짝수라면 L2에서, 홀수라면 L3에서 시작
if N % 2 == 0 :
    L2.append(L1.pop())
    k += 1
else :
    L3.append(L1.pop())
    k += 1


hanoiTop(L1, L2, L3)
print(k)