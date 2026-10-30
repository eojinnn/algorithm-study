a,b,c,d,e,f = map(int,input().split())
found = False
for x in range(-999,1000,1):
    if found == True:
        break
    for y in range(-999,1000,1):
        if a*x + b*y == c and d*x+e*y == f:
            print(x, y)
            found = True
            break
