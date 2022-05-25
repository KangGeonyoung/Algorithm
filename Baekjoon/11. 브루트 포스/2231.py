N = int(input())
result = -1

# input의 자릿수 합을 구하는 코드
def unit(n) :
    unit = 0
    while n > 0 :
        unit += n % 10
        n = n // 10

    return unit

start = 0
end = N

# 생성자를 찾는 과정 (0부터 찾는거라 효율적이지는 않을 듯)
for i in range(start, end + 1) :
    if i + unit(i) == N :
        result = i
        break

if result == -1 :
    print(0)
else :
    print(result)