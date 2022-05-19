N = int(input())
row = 0
col = 0


starList = [[0 for j in range(N)] for i in range(N)]

def blank(n) :
    global row, col
    print(f"blank's n = {n}")
    if n == 1 :
        starList[row][col] = " "
        col += 1
        print("blank")
        print(f"row : {row}, col : {col}")
        return 0
    else :
        return blank(n/3)

def line(n) :
    global row, col
    if n == 1 :
        row += 1
        col -= 3

    print("line")
    print(f"row : {row}, col : {col}")
    return 0

def initial() :
    global row, col
    # 한 줄을 모두 출력했다면 다음 줄로 넘어가는 코드
    if col == N :
        col = 0
        row += 1
    # 아직 한 줄 출력 중이라면
    else :
        row -= 2
    print("initial")
    print(f"row : {row}, col : {col}")
    return 0

def star(n) :
    global row, col
    if n == 1 :
        starList[row][col] = "*"
        col += 1
        print("star")
        print(f"row : {row}, col : {col}")       
        return 0
    else :
        return star(n/3) + star(n/3) + star(n/3) + line(n/3) + star(n/3) + blank(n/3) + star(n/3) + line(n/3) + star(n/3) + star(n/3) + star(n/3) + initial()

star(N)

for i in range(N) :
    for j in range(N) :
        print(starList[i][j], end='')
    print()