def factorial(num, total) :
    if num == 0 :
        return total
    total *= num
    return factorial(num-1, total)

N = int(input())

print(factorial(N, 1))