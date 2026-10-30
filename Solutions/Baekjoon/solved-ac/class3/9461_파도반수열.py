"""
아이디어
p[n] = p[n-1]+ p[n-5]
시간복잡도
O(N)
자료구조
p = []
"""
import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    p = [0,1,1,1,2,2]
    for j in range(6,N+1):
        p.append(p[j-1]+p[j-5])
    print(p[N])

