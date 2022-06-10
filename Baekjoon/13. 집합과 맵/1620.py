import sys
pokemon = dict()
quiz = list()

N, M = map(int, sys.stdin.readline().split())

for i in range(N) :
    pokemon[i+1] = input()

for i in range(M) :
    quiz.append(input())

reverse_pokemon = dict(map(reversed, pokemon.items()))

for i in range(M) :
    if str(quiz[i]).isdigit():
        print(pokemon[int(quiz[i])])
    else :
        print(reverse_pokemon[str(quiz[i])])
