def solve(a : list) :
    total = 0
    for i in range(len(a)) :
        total += a[i]
    return total

a = [1,2,3,4,5,6,7,8,9,10]
print(solve(a))