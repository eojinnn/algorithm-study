A = [list(map(int,input().split())) for i in range(3)]
num = A[0][0]
for i in range(3):
    for j in range(3):
        if num<=A[i][j]:
            num = A[i][j]
            line = i
            row = j
print(num)
print(line, row)
