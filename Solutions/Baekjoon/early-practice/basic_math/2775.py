"""입력
첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

출력
각각의 Test case에 대해서 해당 집에 거주민 수를 출력하라."""
import math
T = int(input())
for i in range(1,T+1):
    K = int(input())
    N = int(input())
    n = K+N
    r = N-1
    print(int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r))))
    


