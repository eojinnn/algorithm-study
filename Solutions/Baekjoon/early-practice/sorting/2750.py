"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다."""

# N = int(input())
# comp = []
# comp_num = 0
# for i in range(N):
#     num = int(input())
#     comp.append(num)
# for cnt in range(len(comp)):
#     for x in range(1,len(comp)):
#         if comp[x] < comp[x-1]:
#             alt = comp[x]
#             comp[x] = comp[x-1]
#             comp[x-1] = alt
# for x in comp:
#     print(x)

N = int(input())
comp=[int(input()) for i in range(N)]

comp.sort(reverse = False)
for i in comp:
    print(i)

         