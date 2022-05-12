from cmath import sqrt


def Gold():
    # 2부터 비교할 것이기 때문에 0번째, 1번째는 False 처리함
    lst = [False, False] + [True] * 10000

    # 10000의 제곱근(루트 씌운 값)까지 비교할 것이기 때문에 m 생성
    m = int(10000 ** 0.5)
    for i in range(2, m+1) :
        if lst[i] == True :
            for j in range(i+i, 10001, i) :
                lst[j] = False

    # 테스트케이스 만큼 반복
    T = int(input())
    for i in range(T) :
        n = int(input())
        
        # 입력 받은 값을 반으로 나눠 중간에서부터 비교하는 방식임
        A = n // 2
        B = A

        for j in range(10000) :
            # 둘 다 소수라면 출력하고 break
            if lst[A] and lst[B] :
                print(A, B)
                break
            # 소수가 아니라면 작은 값부터 출력해야 하기 때문에 A에는 -1, B에는 +1
            A -= 1
            B += 1

Gold()