N = int(input())

for i in range(N) :
    star = ""
    for j in range(N) :
        if i + j >= N-1 :
            star += "*"
        else :
            star += " "
    print(star)