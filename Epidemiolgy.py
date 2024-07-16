# 각 라인은 양의 정수이다
# 한사람이 두번 감염되지 않는다
# 감염된 사람 P < = 10의 7제곱
# *첫 0일에 감염자수 N <= P, *한명이 감염시킬 수 있는 사람 수 R < = 10

P = int(input())
N = int(input())
R = int(input())

total_infected = N
current_infected = N
day = 0

# while문을 사용하여 질병 확산 계산
while total_infected <= P:
    day += 1
    new_infected = current_infected * R
    total_infected += new_infected
    current_infected = new_infected

# 결과 출력
print(day)


