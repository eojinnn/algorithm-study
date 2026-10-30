import heapq
import sys

input = sys.stdin.readline
N = int(input())
heap = []

for i in range(N):
    x = -int(input())
    if x == 0 and len(heap) == 0:
        print(0)
    elif x == 0 and len(heap) != 0:
        maxval = heapq.heappop(heap)
        print(-maxval)
    else:
        heapq.heappush(heap,x)
    