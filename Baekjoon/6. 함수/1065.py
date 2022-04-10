N = int(input())

def findHansu(N) :
    digit = []
    result = 0

    for i in range(1, N + 1) :
        digit.clear()
        num = i
        digit.append(num % 10)
        num = num // 10

        while num > 0 :
            digit.append(num % 10)
            num = num // 10

        # 한 자릿수 또는 두 자릿수 일때
        if len(digit) == 1 or len(digit) == 2:
            result += 1
            continue

        # 세 자릿수부터는 여기에서 한수인지 검사
        calculate = digit[0] - digit[1]
        isHansu = False

        for j in range(len(digit) - 1) :
            if digit[j] - digit[j+1] != calculate :
                isHansu = False
                break
            else :
                calculate = digit[j] - digit[j+1]
                isHansu = True
        
        if isHansu == True :
            result += 1
    
    return result

print(findHansu(N))