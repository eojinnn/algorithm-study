# import sys
# N = int(sys.stdin.readline())
# arr = [0]*10000 # 배열 크기 설정

# for i in range(N):
#     num = int(sys.stdin.readline())
#     arr[num-1] = arr[num-1] + 1 # 수 카운팅

# for j in range(len(arr)):
#     if arr[j] != 0:
#         for x in range(arr[j]):
#             print(j+1) 
    
import sys
N = int(sys.stdin.readline())
arr = [0]*10000 # 배열 크기 설정

for i in range(N):
    num = int(sys.stdin.readline())
    arr[num] = num

for j in arr:
    if j != 0:
        print(j)


