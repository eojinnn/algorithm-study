# """
# 아이디어
# zeros = Zn = Zn-1 + Zn-2 초기값 [1,0,1]
# ones = On = On-1 + On-2 초기값 [0,1,1]

# 시간복잡도
# O(2N*T)
# 자료구조

# """
# import sys
# input = sys.stdin.readline

# T = int(input())

# for i in range(T):
#     n = int(input())
#     zeros = [1,0,1]
#     ones = [0,1,1]
#     for j in range(3, n+1):
#         zeros.append(zeros[j-1]+zeros[j-2])
#         ones.append(ones[j-1]+ones[j-2])
#     print(zeros[n], ones[n])
    

"""
아이디어
ones[n], ones[n-1]출력력

시간복잡도
O(N*T)
자료구조

"""
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    ones = [0,1,1]
    if n == 0:
        print(1, 0)
        continue
    for j in range(3, n+1):
        ones.append(ones[j-1]+ones[j-2])
    print(ones[n], ones[n-1])