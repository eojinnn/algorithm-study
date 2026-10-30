"""
아이디어
종류수 곱하기 -1
시간복잡도
자료구조
"""
import sys

input = sys.stdin.readline
T = int(input())
for i in range(T):
    n = int(input())
    dic = {}
    for j in range(n):
        cl, ca = input().split()
        if ca in dic.keys():
            dic[ca].append(cl)
        else:
            dic[ca] = [cl]
    sum = 1
    for j in dic.keys():
        sum = sum * (len(dic[j])+1)
    print(sum-1)



        
