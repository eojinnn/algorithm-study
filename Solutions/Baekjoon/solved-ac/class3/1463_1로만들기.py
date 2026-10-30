"""
아이디어
3으로 나누고, 2로 나누고, 1로 뺀 값 중에 가장 최단 경로인 값 선택택
시간 복잡도
O(N)?
자료구조
"""
import sys
input = sys.stdin.readline
cnt = N = int(input())
num = [0,0,1,1]
for n in range(4, N+1):
    cnt = num[n-1]+1
    if n%2 == 0:
        cnt = min(cnt, num[n//2]+1)
    if n%3 == 0:
        cnt = min(cnt, num[n//3]+1)
    num.append(cnt)
print(num[N])