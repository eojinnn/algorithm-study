# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 
# 당신은 그들에게 슬픈 진실을 알려줘야 한다.

# 입력
# 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

# 둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
import statistics
C = int(input())
for i in range(C):
    num = 0
    li = list(map(int,input().split()))
    avg = statistics.mean(li[1:]) # avg = mean(100,95,90 80 70 60 50)
    for k in li[1:]:
        if k>avg:
            num += 1
    ratio = float((num/li[0])*100) #li[0] = 7 //1/3*100 = 
    print('%.3f%%' %ratio)

            