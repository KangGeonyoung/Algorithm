# 나이 순으로 정렬하다가 같은 나이가 나올 경우 input으로 들어온 순서대로 정렬
# 새롭게 배운 내용 : int 정렬과 string 정렬의 결과가 다르다.
# ex) 20과 9를 비교해볼때 int 정렬 = [9, 20], string 정렬 = [20, 9] 의 결과가 나오게 됨.

N = int(input())
member = [[0 for col in range(3)] for row in range(N)]

for i in range(N) :
    member[i][0], member[i][1] = input().split()
    member[i][0] = int(member[i][0])
    member[i][2] = i

member.sort(key=lambda x:(x[0], x[2]))

for i in range(N) :
    print(f"{member[i][0]} {member[i][1]}")
