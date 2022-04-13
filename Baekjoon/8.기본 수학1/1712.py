A, B, C = map(int, input().split())
result = -1

if B < C :
    value = C - B
    BEP = int(A / value) + 1
    result = BEP
else :
    result = -1

print(result)