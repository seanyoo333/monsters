# P <= 107
total_infected = int(input())

# N <= P
day0_infected = int(input())

#  R < = 10
infecting_per_one = int(input())

# 변수 초기화
current_infected = day0_infected
count_days = 0
previous_infected = day0_infected

while current_infected <= total_infected:
    count_days += 1
    new_infected = previous_infected * infecting_per_one
    current_infected += new_infected
    previous_infected = new_infected

print(count_days)
