# 중복을 삭제하기 위해서 set을 사용함.
# string[i : j]를 사용하여 잘라서 set에 add해줌
import sys

S = sys.stdin.readline().strip()
wordSet = set()

for i in range(1, len(S) + 1) :
    for j in range(len(S) + 1 - i) :
        wordSet.add(S[j : j+i])

print(len(wordSet))