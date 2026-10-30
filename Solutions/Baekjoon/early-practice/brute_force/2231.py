n = int(input())
r = 0
c = 0
for i in range(n):
    sum = i
    for a in str(i):
        sum = sum + int(a)
    if sum == n:
        c = 1
        print(i)
        break
if c == 0:
    print(0)
