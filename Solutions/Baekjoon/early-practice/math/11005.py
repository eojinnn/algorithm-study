"""
문제
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.

10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35

입력
첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36) N은 10억보다 작거나 같은 자연수이다.

출력
첫째 줄에 10진법 수 N을 B진법으로 출력한다.

예제 입력 1 
60466175 36
예제 출력 1 
ZZZZZ
"""

N,B = map(int,input().split())
"""
진수 변환 : 진법으로 나눈 나머지들을 차례로 밑에서부터 이어 붙인다.
modular 계산 : 60466175mod36 = 35(Z)
map(func, iterable)
"""
alphabet = {i-ord('A')+10 : chr(i) for i in range(ord('A'),ord('Z')+1)}
"""
조건부 딕셔너리 생성
"""
modular = N
output = []
while modular >= B:
    output.append(modular%B)
    modular = modular//B  
output.append(modular)
print(output)
"""
print(alphabet.get(i) for i in output[-1:])
제너레이터 표현식 vs 리스트 컴프리헨션
제너레이터 표현식은 이터러블을 반환하며,
이는 직접 출력하려 할 때 그 내용이 아니라 제너레이터 객체에 대한 정보만 출력됩니다.
<generator object <genexpr> at 0x0000025EC97B8D60>
즉, 제너레이터 자체를 출력하기 때문에 결과가 저렇게 나오는가봄
"""
for i in output[::-1]:
    if i>=10:
        print(alphabet.get(i),end='')
    else:
        print(i, end = '')
"""
리스트 슬라이싱
줄바꿈없이 출력하는 방법
"""