result = []
while True :
    try :
        a, b = map(int, input().split())
        result.append(a+b)
    except :
        break

i = 0
while i < len(result) :
    print(result[i])
    i += 1