N, M = map(int, input().split())
card = list(map(int, input().split()))
num = []

for i in range(0, N-2) :
    for j in range(1, N-1) :
        for k in range(2, N) :
            # 같은 카드가 겹치는 경우
            if i == j or i == k or j == k :
                continue

            # 카드 3장 더한 값이 M 값보다 작은 경우 
            if card[i] + card[j] + card[k] <= M:
                num.append(card[i] + card[j] + card[k])

print(max(num))