import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split(' ')))
P.sort(reverse = False)
cnt = 0
c_list = []
for i in range(len(P)):
    if i == N:
        break
    cnt = cnt + P[i]
    c_list.append(cnt)
print(sum(c_list))
