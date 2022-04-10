word = list(input())
alpha = [['A', 'B', 'C'], ['D', 'E', 'F'], 
['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], 
['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], 
['W', 'X', 'Y', 'Z']]

print(word)

for i in range(len(word)) :
    print(alpha.index(word[i]))
