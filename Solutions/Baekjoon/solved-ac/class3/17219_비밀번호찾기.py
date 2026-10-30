import sys

N, m = map(int, sys.stdin.readline().split())
password_dict = {}
for _ in range(N):
    site, pw = sys.stdin.readline().split()
    password_dict[site] = pw
for _ in range(m):
    roi = sys.stdin.readline().strip()
    print(password_dict[roi])