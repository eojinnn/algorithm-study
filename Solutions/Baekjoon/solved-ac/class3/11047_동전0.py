import sys
N, K = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline().strip()) for _ in range(N)]
A.sort(reverse = True)

cnt= 0
for i in range(len(A)):
    if K == 0:
        break
    if K >= A[i]:
        cnt = cnt + K//A[i]
        K = K-cnt*A[i]
print(cnt)