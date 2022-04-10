selfNumber = []
size = 10000

def d(n) :
    result = n
    result += n % 10
    n = n // 10
    while n > 0 :
        result += n % 10
        n = n // 10
    return result

for i in range(size) :
    selfNumber.append(i+1)

# 숫자 101의 경우 생성자가 2개여서 remove가 두번 발동함. => 에러 발생
# => list에 있는 count 함수를 이용해 list 속에 해당 값이 있을 때만 삭제하는 걸로 변경
for i in range(1, size + 1) :
    result = d(i)
    if result <= 10000 and selfNumber.count(result) > 0:
        selfNumber.remove(result)
    
for i in range(len(selfNumber)) :
    print(selfNumber[i])