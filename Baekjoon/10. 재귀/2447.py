from cmath import sqrt


N = int(input())
row = 0
col = 0

starList = [["*" for j in range(N)] for i in range(N)]

for i in range(N) :
    for j in range(N) :
        print(starList[i][j], end='')
    print()
    
print()

def eraseStar(n) :
    row = int(n / 3)
    col = int(n / 3)

    for m in range(int(N/n) * int(N/n)) :
        count = 0
        for i in range(int(n/3)) :
            for j in range(int(n/3)) :
                starList[row][col] = " "
                col += 1
                count += 1
            row += 1
            col -= int(n/3)
    eraseStar(n/3)

eraseStar(N)

for i in range(N) :
    for j in range(N) :
        print(starList[i][j], end='')
    print()