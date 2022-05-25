N = int(input())

weight = [0] * N
height = [0] * N
rank = [0] * N

for i in range(N) :
    weight[i], height[i] = map(int, input().split())

for i in range(N) :
    count = 0
    for j in range(N) :
        if i == j :
            continue
        
        if weight[i] < weight[j] and height[i] < height[j] :
            count += 1
        
    rank[i] = count + 1

for i in range(N) :
    print(rank[i])