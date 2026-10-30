tri = list(map(int,input().split()))
if max(tri) >= sum(tri)-max(tri):
    tri[tri.index(max(tri))] = sum(tri)-max(tri) - 1
    print(sum(tri))
else:
    print(sum(tri))
##sorted 쓸수도 있음.