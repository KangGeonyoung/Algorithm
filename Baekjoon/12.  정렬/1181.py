# 단어들을 길이가 짧은 순으로 정렬하다가 길이가 같으면 사전 순으로 정렬
N = int(input())
word = []

for i in range(N) :
    word.append(input())

# set을 이용하여 중복 제거하고 새로운 길이 변수 설정
word = set(word)
size = len(word)

# sort는 list만 가능하기 때문에 다시 list로 변환
word = list(word)

# 길이 순으로 정렬하다가 같은 길이가 나올 경우 사전식으로 정렬
word.sort(key=lambda x:(len(x), x))

for i in range(size) :
    print(word[i])