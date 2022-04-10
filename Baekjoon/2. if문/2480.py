a, b, c = map(int, input().split())

if a == b == c :
    prize = 10000 + a * 1000
elif a == b and b != c :
    prize = 1000 + a * 100
elif a == c and b != c :
    prize = 1000 + a * 100
elif b == c and a != b :
    prize = 1000 + b * 100
elif a != b != c :
    max = a
    if max < b :
        max = b
    if max < c :
        max = c
    prize = max * 100

print(prize)