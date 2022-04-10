T = int(input())
array_a = [0] * T
array_b = [0] * T
result = [0] * T

for i in range(T) : 
    a, b = map(int, input().split())
    array_a[i] = a
    array_b[i] = b
    result[i] = a + b

for i in range(T) :
    print(f"Case #{i+1}: {array_a[i]} + {array_b[i]} = {result[i]}")