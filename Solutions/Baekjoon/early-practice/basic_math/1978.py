"""
문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.
"""
N = int(input())
num = list(map(int,input().split()))
ls = []
for i in range(2,max(num)+1):
    is_prime = True
    for j in range(2,i):#단순반복문
        if i%j == 0:
            is_prime = False
            break
    if is_prime:   
        ls.append(i)
cnt = 0
for k in num:
    if k in ls:
        cnt = cnt+1
print(cnt)
    
