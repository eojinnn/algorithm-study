"""
아이디어

"""
import sys
from collections import Counter

input = sys.stdin.readline

N,M,B = map(int, input().split())
g = []
for i in range(N):
    g.extend(map(int, input().split()))

height_count = Counter(g)
max_val = max(height_count)
min_val = min(height_count)

min_cnt = 500*500*256*2
min_height = 0
for i in range(max_val, min_val-1, -1):
    temp = 0
    cnt = 0
    for h, count in height_count.items():
        diff = i-h
        if diff < 0:
            temp += (-diff*2)*count
        elif diff > 0:
            temp += diff * count
            cnt += diff * count
    if cnt > B:
        continue
    elif temp < min_cnt:
        min_cnt = temp
        min_height = i


print(min_cnt, min_height)



