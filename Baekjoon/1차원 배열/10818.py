N = int(input())
num = list(map(int, input().split()))

max = min = num[0]
for i in range(N) :
    if num[i] > max :
        max = num[i]
    if num[i] < min :
        min = num[i]

print(f"{min} {max}")