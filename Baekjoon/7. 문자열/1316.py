case = int(input())
words = [0] * case
alpha = []
result = 0

for i in range(case) :
    words[i] = list(input())

# 입력 받은 case 수 만큼 반복
for i in range(case) :
    alpha.clear()
    previous = -1
    current = -1
    state = 1

    # 단어의 알파벳 수만큼 반복
    for j in range(len(words[i])) :
        # 알파벳이 alpha list에 없을 경우
        if alpha.count(words[i][j]) == 0 :
            alpha.append(words[i][j])
            previous = current
            current += 1
        # 알파벳이 alpha list에 있을 경우
        else :
            previous = current
            current = alpha.index(words[i][j])
            if current -previous < 0 :
                state = 0
                break
            
    if state == 1 :
        result += 1

print(result)