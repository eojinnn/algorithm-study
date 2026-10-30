x = []
is_Isosceles = False
is_Equilateral = False
for i in range(3):
    a = int(input())
    if a in x:
        if a == 60:
            is_Equilateral = True
        else:
            is_Isosceles = True
    x.append(a)

if sum(x) == 180:
    if is_Equilateral:
        print("Equilateral")
    elif is_Isosceles:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
    