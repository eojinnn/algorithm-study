"""
시간복잡도
NlogN * 
"""

import sys

input = sys.stdin.readline
N, M = map(int, input().split())
x = list(map(int, input().split()))

def search(st, en, target):
    if st > en:  # 기저 조건 (탐색 종료)
        print(en)  # en이 최적의 절단 높이
        return
    
    mid = (st + en) // 2  # 현재 설정할 절단기 높이
    total = sum(l - mid for l in x if l > mid)  # 나무를 얻는 총 길이 계산

    if total < target:
        search(st, mid-1, target)  # 더 많은 나무를 얻기 위해 절단 높이를 낮춘다
    else:
        search(mid+1, en, target)  # 절단 높이를 높여서 더 적은 나무를 얻도록 조정

search(0, max(x), M)

