C = int(input())
Class = [0] * C

for i in range(C) :
    Class[i] = list(map(int, input().split()))

print(Class)