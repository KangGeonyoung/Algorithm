def hanoiTop(L1, L2, L3) :
    global Max, count, N, k

    # 마지막 남은 건 찾아서 L3에 쌓아주기
    if len(L1) == 1 and len(L2) == 0 or len(L1) == 0 and len(L2) == 1:
        if len(L1) > 0 :
            L3.append(L1.pop())
            k += 1
            print("1 3")
        elif len(L2) > 0 :
            L3.append(L2.pop())
            k += 1
            print("2 3")

    # L2나 L3에 빈자리가 생긴다면 채워주기
    if len(L2) == 0 and len(L1) > 1:
        L2.append(L1.pop())
        k += 1
        print("1 2")
    elif len(L3) == 0:
        L3.append(L1.pop())
        k += 1
        print("1 3")
    
    # L1이 빈 상태이고 L2가 2개 이상이라면 L1을 하나 채워준다
    if len(L1) == 0 and len(L2) > 1:
        L1.append(L2.pop())
        print("2 1")
        k += 1

    # 크기를 비교해 쌓아올리는 과정
    if len(L2) > 0 and len(L3) > 0 :
        if L2[-1] - L3[-1] == 1 :
            L2.append(L3.pop())
            k += 1
            print("3 2")
        elif L2[-1] - L3[-1] == -1 :
            L3.append(L2.pop())
            k += 1
            print("2 3")
    
    # L3에 Max값이 들어온 경우 count 추가해주기
    if L3.count(Max) == 1 :
        print("Max count", count)
        Max = L3[-1] - 1
        count += 1

    # 3번 자리에 쌓인 개수에 따라서 함수 반복
    if count != N-1 :
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
    print("1 2")
else :
    L3.append(L1.pop())
    k += 1
    print("1 3")


hanoiTop(L1, L2, L3)

print(L1, L2, L3)
print(k)