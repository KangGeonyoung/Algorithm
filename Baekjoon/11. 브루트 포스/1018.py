row, col = map(int, input().split())
board = [0] * row

BcntRow = [0] * row
WcntRow = [0] * row
diffRow = [0] * row

BcntCol = [0] * col
WcntCol = [0] * col
diffCol = [0] * col

# input 입력 과정
for i in range(row) :
    board[i] = list(input())

# row 검사
for i in range(row) :
    for j in range(col) :
        if board[i][j] == 'B' :
            BcntRow[i] += 1
        elif board[i][j] == 'W' :
            WcntRow[i] += 1

# row마다 W와 B의 개수 차이를 계산하는 코드
for i in range(row) :
    diffRow[i] = abs(WcntRow[i] - BcntRow[i])

# row의 start 지점을 찾아주는 코드
for i in range(row - 8 + 1) :
    total = 0
    for j in range(i, 8 + i) :
        total += diffRow[j]
    
    if i == 0 :
        minTotal = total
        startRow = i

    if total < minTotal :
        minTotal = total
        startRow = i


# col 검사
for i in range(col) :
    for j in range(startRow, startRow + 8) :
        if board[j][i] == 'B' :
            BcntCol[i] += 1
        elif board[j][i] == 'W' :
            WcntCol[i] += 1

# col마다 W와 B의 개수 차이를 계산하는 코드
for i in range(col) :
    diffCol[i] = abs(WcntCol[i] - BcntCol[i])

# col의 start 지점을 찾아주는 코드
for i in range(col - 8 + 1) :
    total = 0
    for j in range(i, 8 + i) :
        total += diffCol[j]
    
    if i == 0 :
        minTotal = total
        startCol = i

    if total < minTotal :
        minTotal = total
        startCol = i

print(f"startRow = {startRow}, startCol = {startCol}")

# startRow, startCol로부터 8*8 범위 안에 있는 보드판을 검사
if board[startRow][startCol] == 'B' :
    color = 'B'
    boardNum = 0



 
   




