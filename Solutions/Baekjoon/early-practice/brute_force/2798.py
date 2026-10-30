N, M = map(int,input().split())
n = list(map(int,input().split()))
sum = 0
for i in range(len(n)):
    for j in range(len(n)):
        if j == i:
            continue
        else:
            for k in range(len(n)):
                if j == k or i ==k:
                    continue
                else:
                    if sum < n[i]+n[j]+n[k] <= M:
                        sum = n[i]+n[j]+n[k]
                    else:
                        continue

print(sum)

    