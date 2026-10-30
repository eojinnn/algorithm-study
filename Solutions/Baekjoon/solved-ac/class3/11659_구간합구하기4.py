"""
아이디어
정적 배열-> 누적합prefix sum( 구간 쿼리 )
시간복잡도
10만*1
자료구조
a = [10만], psum = []
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
N = [0] + list(map(int, input().split()))

psum = [0]
for i in range(1, n):
    psum.append(psum[i-1]+N[i])
for c in range(m):
    i, j = map(int,input().split())
    print(psum[j]-psum[i-1])