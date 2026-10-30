# while 1:
#     n = int(input())
#     if n == -1:
#         break
#     multiples = []
#     for i in range(1, n):   
#         if n%i == 0:
#             multiples.append(i)
#     if sum(multiples) == n:
#         print(str(n) + " = 1", end="")
#         for j in multiples[1:]:
#             print(" + %d" %j, end='')
#         print('')
#     else:
#         print("%d is NOT perfect." %n)
while True:
    n = int(input())
    if n == -1: # 입력 값이 -1이면 반복문 종료
        break;
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(n, " = ", " + ".join(str(i) for i in arr), sep="")
    else:
        print(n, "is NOT perfect.")