import sys

x, y, w, h = map(int, sys.stdin.readline().split())

xMin = min(x, w-x)
yMin = min(y, h-y)

result = min(xMin, yMin)
print(result)