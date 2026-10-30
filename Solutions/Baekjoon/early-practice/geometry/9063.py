N = int(input())
corx = []
cory = []
for i in range(N):
    x, y = map(int, input().split())
    corx.append(x)
    cory.append(y)

d = (max(corx)-min(corx))*(max(cory)-min(cory))
print(d)