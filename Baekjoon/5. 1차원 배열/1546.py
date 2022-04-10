N = int(input())
grade = list(map(float, input().split()))
total = 0

Max = max(grade)
for i in range(N) :
    grade[i] = grade[i] / Max * 100
    total += grade[i]

print(float(total/N))