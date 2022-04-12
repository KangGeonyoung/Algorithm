word = list(input())
croatia = [['c','='],
    ['c','-'], ['d','z','='],
    ['d','-'], ['l','j'],
    ['n','j'], ['s','='],
    ['z','=']]

i = 0
result = 0

# 단어의 알파벳 개수 만큼 반복
while i < len(word) :
    # croatia list의 묶음 개수 만큼 반복
    for j in range(len(croatia)) :
        correctState = 0
        # croatia 단어들의 첫 글자만 비교
        if word[i] == croatia[j][0]:
            # 모두 일치하는지 확인하는 반복문
            for k in range(len(croatia[j])) :
                # indexof 에러 발생 예방
                if i+k > len(word)-1 :
                    correctState = 0
                    break
                if word[i+k] == croatia[j][k] :
                    correctState = 1
                else :
                    correctState = 0
                    break

            if correctState == 1 :
                result += 1
                i += len(croatia[j])
                break
    
    if correctState == 0 :
        result += 1
        i += 1

print(result)