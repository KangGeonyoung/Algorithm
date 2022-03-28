word = input()

lst = list(word)
result = [-1] * 26

for i in range(26) :
    # 알파벳이 단어 속에 있다면 if문 실행
    if lst.count(chr(97 + i)) > 0 :
        position = 0
        for j in range(len(lst)) :
            if chr(97 + i) == lst[j] :
                break
            else :
                position += 1
        result[i] = position
    else :
        result[i] = -1

output = ""
for i in range(26) :
    output += str(result[i]) + " "

print(output)