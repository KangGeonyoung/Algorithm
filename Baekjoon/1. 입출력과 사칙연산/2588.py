first = int(input())
second = int(input())

second_1 = second % 10
second = second // 10

second_2 = second % 10
second = second // 10

second_3 = second % 10
second = second // 10

result1 = first * second_1
result2 = first * second_2
result3 = first * second_3

result4 = result1 + result2 * 10 + result3 * 100

print(result1)
print(result2)
print(result3)
print(result4)