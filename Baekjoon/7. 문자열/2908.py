a, b = map(int, input().split())

def reverseNum(num) :
    num = (num // 100) + ((num % 100) // 10) * 10 + (num % 10) * 100
    return num

a = reverseNum(a)
b = reverseNum(b)

print(max(a, b))