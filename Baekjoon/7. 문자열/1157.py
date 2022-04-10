word = list(input().upper())
alpha = []
count = []

for i in range(len(word)) :
    added = 0
    for j in range(len(alpha)) :
        if ord(word[i]) == ord(alpha[j]) :
            count[j] += 1
            added = 1
            
    # 해당 알파벳이 처음 보는 알파벳이라면 list에 추가하기
    if added == 0 :
        alpha.append(word[i])
        count.append(1)
        added = 1

# 가장 많이 사용된 알파벳이 1개라면
if count.count(max(count)) == 1 :
    print(alpha[count.index(max(count))])
# 1개가 아니라면
else :
    print("?")