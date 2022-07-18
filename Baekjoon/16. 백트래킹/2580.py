import sys

def sudoku(i, j) :
    row = list()
    col = list()
    square = list()

    # row에서 없는 숫자 검사
    number = [1,2,3,4,5,6,7,8,9]
    for m in range(9) :
        if board[i][m] in number :
            number[number.index(board[i][m])] = 0
    for m in range(9) :
        if number[m] != 0 :
            row.append(number[m])

    # col에서 없는 숫자 검사
    number = [1,2,3,4,5,6,7,8,9]
    for m in range(9) :
        if board[m][j] in number :
            number[number.index(board[m][j])] = 0
    for m in range(9) :
        if number[m] != 0 :
            col.append(number[m])

    # 3*3 사각형에서 없는 숫자 검사
    number = [1,2,3,4,5,6,7,8,9]
    start_row = i // 3 * 3
    start_col = j // 3 * 3

    for m in range(3) :
        for n in range(3) :
            if board[start_row + m][start_col + n] in number :
                number[number.index(board[start_row + m][start_col + n])] = 0
    for m in range(9) :
        if number[m] != 0 :
            square.append(number[m])

    # 3개의 검사 결과 중에 중복되는 숫자 추출
    intersection = list(set(row) & set(col) & set(square))
    print(f"intersection : {intersection}")

    # 찾은 숫자 보드에 대입
    if len(intersection) > 0 :
        board[i][j] = intersection[0]

    # 종료
    return

# 스도쿠 보드 세팅
board = [[0 for col in range(9)] for row in range(9)]

# input 입력 받는 코드
for i in range(9) :
    board[i] = list(map(int, sys.stdin.readline().split()))

# 0을 발견하면 sudoku 함수 실행
for i in range(9) :
    for j in range(9) :
        if board[i][j] == 0 :
            sudoku(i, j)

# 스도쿠 결과 출력
for i in range(9) :
    for j in range(9) :
        print(board[i][j], end=" ")
    print()
