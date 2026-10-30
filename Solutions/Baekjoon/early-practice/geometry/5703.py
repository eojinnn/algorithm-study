while 1:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    elif x+y >z and x+z>y and y+z>x: 
        if x==y==z:
            print("Equilateral")
        elif x==y or y==z or x==z:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")


