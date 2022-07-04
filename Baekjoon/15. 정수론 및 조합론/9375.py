import sys

T = int(sys.stdin.readline())

for i in range(T) :
    case = int(sys.stdin.readline())
    clothesDict = dict()
    clothesType = list()

    for j in range(case) :
        clothes =  list(sys.stdin.readline().split())

        # 옷 종류별로 개수 세는 코드
        if clothes[1] in clothesDict :
            clothesDict[clothes[1]] += 1
        else : 
            clothesDict[clothes[1]] = 1
            clothesType.append(clothes[1])
    
    # ( 종류a의 옷 개수 + 1 ) ( 종류 b의 옷 개수 + 1) .... -1
    # +1의 의미 : 그 종류의 옷을 입지 않을 경우의 수
    # -1의 의미 : 모든 종류의 옷을 입지 않을 경우의 수
    # 옷 개수 자체가 경우의 수가 된다. 따라서 그 옷을 입지 않을 경우의 수인 1이 추가되는 것이다.
    # 경우의 수를 모두 곱하면 옷을 전부 입지 않는 수가 나오는데 그걸 빼주기 위해 -1을 한 것

    result = 1
    for j in range(len(clothesDict)) :
        result *= (clothesDict[clothesType[j]] + 1)
    result -= 1

    print(result)
