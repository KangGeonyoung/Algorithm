# min이나 max에도 key를 이용하여 함수를 넣는 것이 가능하다.
import sys

x = [0] * 3
y = [0] * 3

for i in range(3) :
    x[i], y[i] = map(int, sys.stdin.readline().split())

result_x = min(x, key=x.count)
result_y = min(y, key=y.count)
print(f"{result_x} {result_y}")
