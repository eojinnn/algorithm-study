import time
import sys
from collections import Counter
N = int(sys.stdin.readline())
li = []

for i in range(N):
    li.append(int(sys.stdin.readline()))
    
li.sort(reverse = False) # 내림차순 정렬

def mode(nums):
    c = Counter(nums)
    mod = c.most_common() # 최빈값
    maximum = mod[0][1]
    arr = []
    j = 0
    for j in range(len(mod)):
        if maximum == mod[j][1]:
            arr.append(mod[j][0])
        
    if len(arr) >= 2:
        return arr[1]
    else:
        return arr[0]

print(int(round(sum(li)/N,0)))
print(li[N//2])
print(mode(li))
print(max(li)-min(li))

#-2 1 2 3 8
start_time = time.time()
elapsed_time = time.time() - start_time
print("Elapsed time: %0.10f seconds" %elapsed_time)
