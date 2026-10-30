import sys

input = sys.stdin.readline
N = int(input())
g = []
for i in range(N):
    row = list(map(int, input().split()))
    g.append(row)

def funct(n, g, wcnt, bcnt):
    target = g[0][0]
    if all(all(val == target for val in row) for row in g):
        if target == 1:
            bcnt += 1
        elif target == 0:
            wcnt += 1
        return wcnt, bcnt
    else:
        n = n//2
        g1 = [row[:n] for row in g[:n]]  # 좌상단
        g2 = [row[n:] for row in g[:n]]  # 우상단
        g3 = [row[:n] for row in g[n:]]  # 좌하단
        g4 = [row[n:] for row in g[n:]]  # 우하단

        wcnt1, bcnt1 = funct(n, g1, wcnt, bcnt)
        wcnt2, bcnt2 = funct(n, g2, wcnt, bcnt)
        wcnt3, bcnt3 = funct(n, g3, wcnt, bcnt)
        wcnt4, bcnt4 = funct(n, g4, wcnt, bcnt)
        wcnt = wcnt1+wcnt2+wcnt3+wcnt4
        bcnt = bcnt1+bcnt2+bcnt3+bcnt4
        return wcnt, bcnt
    
wcnt = 0
bcnt = 0
wcnt, bcnt = funct(N, g, wcnt,bcnt)
print(bcnt)
print(wcnt)


        


