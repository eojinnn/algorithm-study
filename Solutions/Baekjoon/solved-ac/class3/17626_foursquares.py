'''
아이디어
제곱수들의 리스트만들기 그 수보다 작은 제곱수 빼가면서 최소가 되는 제곱수들의 합
시간복잡도

'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*50005
for i in range(1, n+1):
    dp[i] = dp[i-1]+1
    j = 1
    while j*j <= i:
        dp[i] = min(dp[i], dp[i-j*j]+1)
        j = j+1
print(dp[n])