"""
아이디어
dp[n] = dp[n-1]+dp[n-2]+dp[n-3]
시간 복잡도
O(N)?
자료구조
"""
import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    n = int(input())
    dp = [0, 1, 2, 4]
    for j in range(4, n+1):
        dp.append(dp[j-1]+dp[j-2]+dp[j-3])
    print(dp[n])

