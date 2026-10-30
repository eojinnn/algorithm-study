import sys
N = list(map(int,str(input())))
N.sort(reverse = True)
result = ''.join(str(x) for x in N)
print(result)
