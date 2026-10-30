# cnt = int(input())
# Rec = []
# for i in range(cnt):
#     R,L = map(int,input().split())
#     for j in range(L,L+10):
#         for k in range(100*j+R,100*j+R+10):
#             if k not in Rec:
#                 Rec.append(k)
# print(len(Rec))
# import numpy as np
# li = np.array([])
# cnt = int(input())
# for i in range(cnt):
#     A, B = map(int,input().split())
#     for k in range(B,B+10):
#         for j in range(A,A+10):
#             if [j,k] not in li:
#                 li = np.vstack(li,np.array([j,k]))
# print(li)

li = []
cnt = int(input())
for i in range(cnt):
    x, y = map(int,input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            li.append(list([j,k]))
    nli = list(set([tuple(coordinates) for coordinates in li]))
print(len(nli))
    



    

