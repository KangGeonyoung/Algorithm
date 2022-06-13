import sys

S = sys.stdin.readline().strip()
wordSet = set()

for i in range(1, len(S) + 1) :
    for j in range(len(S) + 1 - i) :
        wordSet.add(S[j : j+i])

print(len(wordSet))