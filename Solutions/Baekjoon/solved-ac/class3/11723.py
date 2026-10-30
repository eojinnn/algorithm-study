def add(x= 0, S= {}):
    if x in S:
        return S
    else:
        S.add(x)
    return S

def remove(x=0, S = {}):
    if x in S:
        S.remove(x)
        return S
    else:
        return S
    
def check(x, S):
    if x in S:
        print('1')
        return S
    else:
        print('0')
        return S

def toggle(x, S):
    if x not in S:
        S.add(x)
    else:
        S.remove(x)
    return S

def all(S):
    S.update(range(1,21))
    return S

def empty(S):
    S = S.clear()
    
import sys
M = int(sys.stdin.readline())

S = set()
for epoch in range(M):
    command = sys.stdin.readline().split()
    if len(command) == 2:
        func, n = command[0], int(command[1])
    else:
        func = command[0]
    if func == 'add':
        add(n, S)
    elif func == 'remove':
        remove(n, S)
    elif func == 'check':
        check(n, S)
    elif func == 'toggle':
        toggle(n, S)
    elif func == 'all':
        all(S)
    else:
        empty(S)
    
    




