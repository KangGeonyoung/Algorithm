word = list(input())
alpha = [['A', 'B', 'C'], ['D', 'E', 'F'], 
['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], 
['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], 
['W', 'X', 'Y', 'Z']]
result = 0

# 입력된 단어의 알파벳 개수만큼 반복
for i in range(len(word)) :
    # alpha list의 묶음 개수만큼 반복
    for j in range(len(alpha)) :
        # alpha list의 묶음 속 알파벳 개수만큼 반복
        for k in range(len(alpha[j])) :
            if alpha[j][k] == word[i] :
                result += j + 3
                break

print(result)