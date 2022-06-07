# y좌표로 오름차순 정렬하다가 같은 값이 나올경우 
# x좌표로 오름차순 정렬
N = int(input())
xy = [[0 for col in range(2)] for row in range(N)]

for i in range(N) :
    xy[i][0], xy[i][1] = map(int, input().split())

xy.sort(key=lambda x:(x[1], x[0]))


for i in range(N) :
    print(f"{xy[i][0]} {xy[i][1]}")
