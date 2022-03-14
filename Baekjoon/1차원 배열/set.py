#3052 다른 방법
#set은 중복제거 특징이 있음
res = []

for i in range(10) :
    res.append(int(input()) % 42)

result = set(res)
print(len(result))