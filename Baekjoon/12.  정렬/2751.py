N = int(input())
num = []

for i in range(N) :
    num.append(int(input()))

num.sort(reverse = False)

for i in range(N) :
    print(num[i])