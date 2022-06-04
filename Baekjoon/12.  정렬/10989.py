# 메모리 제한 : 8MB
# N은 최대 10000000개이기 때문에 sort를 사용하게 되면 메모리 초과 오류가 뜨게 된다.
# 각각의 숫자는 10000이하의 자연수이다.
# 따라서 10001개의 배열을 만들어 input으로 들어온 값들의 count를 올려주면 된다.
import sys

N = int(sys.stdin.readline())
numList = [0] * 10001

for i in range(N) :
    num = int(sys.stdin.readline())
    numList[num] += 1

for i in range(1, 10001) :
    if numList[i] != 0 :
        for j in range(numList[i]) :
            print(i)
