# 소숫점 n자리까지 출력을 해야할 때 f string 변수 괄호 안에 :.nf를 붙이면 된다.
import math

R = int(input())

uclidArea = float(R * R * math.pi)
taxiArea = float(R * R * 2)

print(f"{uclidArea:.6f}")
print(f"{taxiArea:.6f}")