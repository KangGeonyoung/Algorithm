num = [0] * 9
position = [0] * 9

for i in range(9) :
    num[i] = int(input())
    position[i] = i+1

Max = max(num)

for i in range(9) :
    if num[i] == Max :
        result = position[i]

print(Max)
print(result)