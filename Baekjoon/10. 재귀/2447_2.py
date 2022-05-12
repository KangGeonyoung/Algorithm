N = int(input())
row = 0
col = 0


starList = [[0] * N] * N

def blank(n) :
    global row, col
    if n == 1 :
        print("blank")
        starList[row][col] = 0
        col += 1
        return 0
    else :
        return blank(n/3)

def line() :
    global row, col
    row += 1
    col -= 3
    return 0

def initial() :
    global row, col
    row = 0
    return 0

def star(n) :
    global row, col
    if n == 1 :
        starList[row][col] = 1
        col += 1
        return 0
    else :
        return star(n/3) + star(n/3) + star(n/3) + line() + star(n/3) + blank(n/3) + star(n/3) + line() + star(n/3) + star(n/3) + star(n/3) + initial()

star(N)

for i in range(N) :
    for j in range(N) :
        print(starList[i][j], end='')
    print()