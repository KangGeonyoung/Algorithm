from math import ceil

A, B, V = map(int, input().split())

def snail(a, b, v) :
    count = 1
    newB = a - b
    newV = v - a
    count += ceil(float(newV/newB))
    return count

print(snail(A, B, V))

# 실패한 코드들
# def snail(a, b, v) :
#     result = 0
#     count = 0

#     while True:
#         count += 1
#         result += a
#         if result >= v :
#             break
#         result -= b
#     return count

# def snail(a, b, v) :
#     count = v // a
#     result = a * count - b * count

#     while True:
#         count += 1
#         result += a
#         if result >= v :
#             break
#         result -= b
#     return count

# def snail(a, b, v) :
#     return v-(a-b)*b