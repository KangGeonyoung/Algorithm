N = int(input())
num = list(map(int, input().split()))
Min = min(num)

for i in range(len(num)) :
    num[i] += abs(Min)

newNum = set(num)
newNum = list(newNum)

newNum.sort()

# dictionary를 통해 결과 값을 저장
dic = {}
for i in range(len(newNum)) :
    dic[i] = newNum[i]

reverse_dic = dict(map(reversed, dic.items()))

for i in range(N) :
    print(reverse_dic[num[i]], end=' ')
