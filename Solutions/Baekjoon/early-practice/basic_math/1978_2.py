import math
N = int(input())
num = list(map(int,input().split()))
max = max(num)
res = []
chk=[True]*(max+1)
chk[0],chk[1] = False, False 
for i in range(2,int(math.sqrt(max))+1):
    if chk[i]:
        j = 2
        while i*j<=max: 
            chk[i*j]=False
            j = j+1
    res = [x for x in range(max+1) if chk[x]]
print(res)
