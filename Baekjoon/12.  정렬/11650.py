N = int(input())
xy = [[0 for col in range(2)] for row in range(N)]

for i in range(N) :
    xy[i][0], xy[i][1] = map(int, input().split())

xy.sort()

for i in range(N) :
    print(f"{xy[i][0]} {xy[i][1]}")
