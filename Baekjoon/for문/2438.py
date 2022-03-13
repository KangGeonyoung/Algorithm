N = int(input())

for i in range(N) :
    star = ""
    for j in range(i+1) :
        star += "*"
    print(star)