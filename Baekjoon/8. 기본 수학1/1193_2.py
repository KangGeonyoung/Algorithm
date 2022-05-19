# 통과 코드
X = int(input())

n = 1
result = n * (n + 1) / 2
pre = int(result)

# 몇 번째 라인(= n)에 해당하는지 찾는 반복문
while result < X :
    n += 1
    pre = int(result)
    result = n * (n + 1) / 2

if n % 2 == 0 :
    #짝수
    start_x = 1
    start_y = n
    for i in range(X-pre-1) :
        start_x += 1
        start_y -= 1
else :
    #홀수
    start_x = n
    start_y = 1
    for i in range(X-pre-1) :
        start_x -= 1
        start_y += 1

print(f"{start_x}/{start_y}")