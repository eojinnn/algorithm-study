A = []
B = range(1,31)
ans = []
for i in range(0,28):
    A.append(int(input()))
for j in B:
    if j not in A:
        ans.append(j)
print(min(ans))
print(max(ans))

