N, K = map(int, input().split())
multiples = []
for i in range(1, N+1):
    if N%i == 0:
        multiples.append(i)
if len(multiples)>=K:
    print(multiples[K-1])
else:
    print(0)