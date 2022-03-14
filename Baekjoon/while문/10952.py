result = []
a, b = map(int, input().split())

while a != 0 and b != 0 :
    result.append(a + b)
    a, b = map(int, input().split())

i = 0
while i < len(result) :
    print(result[i])
    i += 1