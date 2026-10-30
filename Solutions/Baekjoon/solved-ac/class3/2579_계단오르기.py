"""
아이디어
6번을 밟는 경우의 수 = 5번을 밟을 때 + 5번을 밟지 않을 때
5번을 밟을 때 : 5번값 + 3번을 밟는 경우의 수
5번을 밟지 않을 때 : 4번을 밟는 경우의 수
case[n] = max(10 + case[n-3] , case[n-2])
case[n]은 n번째 계단을 밟을 때의 최대값
시간복잡도
글쎄 O(N)?
자료구조
"""
import sys

write = sys.stdout.write
with open(0) as f:
    floor, *lines = f.read().strip().split('\n')
    floor = int(floor)
    lines = [0] + list(map(int, lines))
    
    if floor == 1:
        print(lines[1])
        exit()
    elif floor == 2:
        print(lines[1] + lines[2])
        exit()
    elif floor == 3:
        print(max(lines[1], lines[2]) + lines[3])
        exit()

    maxval = [0,lines[1], lines[1] + lines[2], max(lines[1], lines[2]) + lines[3]]
    for n in range(4, floor+1):
        maxval.append(max(maxval[n-3]+lines[n-1],maxval[n-2])+lines[n])
    print(maxval[floor])
