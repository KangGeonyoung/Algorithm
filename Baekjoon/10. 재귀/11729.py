# 하노이 함수 실행 중 탑을 옮기는 과정을 리스트에 저장하는 함수
def move(N, start, to) :
    global k
    moveList.append(f"{start} {to}")
    k += 1

# 하노이 함수
def hanoi(N, start, to, via) :
    if N == 1 :
        move(N, start, to)
    else :
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)

# 초기 세팅 및 input 입력 과정
moveList = []
k = 0
N = int(input())
hanoi(N, 1, 3, 2)

# 옮긴 횟수와 옮긴 경로 출력해주는 코드
print(k)
for i in range(k) :
    print(moveList[i])