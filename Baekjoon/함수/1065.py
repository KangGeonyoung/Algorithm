N = int(input())
digit = []
result = 0

def findHansu(N) :
    total = 0

    for i in range(1, N + 1) :
        digit.clear()
        num = i
        digit.append(num % 10)
        num = num // 10

        while num > 0 :
            digit.append(num % 10)
            num = num // 10

        if len(digit) == 1 or len(digit) == 2:
            result += 1
            continue

        calculate = digit[0] - digit[1]

        for j in range(len(digit) - 1) :
            if digit[j] - digit[j+1] != calculate :
                break
            else :
                calculate = digit[j] - digit[j+1]
