result = [0] * 10
a = int(input())
b = int(input())
c = int(input())
cal = a*b*c

while cal > 0 :
    digit = cal % 10
    cal = cal // 10
    result[digit] += 1

for i in range(10) :
    print(result[i])