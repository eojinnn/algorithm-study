N = int(input())
cnt = 0
n = 666
while cnt <= N:
    if '666' in str(n):
        cnt += 1
    if cnt == N:
        print(str(n))
        break
    n = n+1

