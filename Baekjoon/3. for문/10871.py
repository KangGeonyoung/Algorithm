N, X = map(int, input().split())
result = []
output = ""
num = input().split()

for i in range(N) :
    num[i] = int(num[i])

for i in range(N) :
    if num[i] < X :
        result.append(num[i])

for i in range(len(result)) :
    output += str(result[i]) + " "

print(output)