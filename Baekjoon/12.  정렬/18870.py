N = int(input())
num = list(map(int, input().split()))

newNum = set(num)
newNum = list(newNum)

newNum.sort()

for i in range(N) :
    print(newNum.index(num[i]) ,end=' ')