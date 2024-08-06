# 1 <= N <= 100 / * 7
question_num = int(input())
# A, B, C 문자만 사용 / * BACCCAC
given_answer = input()

Adrian_pattern = 'ABC'
Bruno_pattern = 'BABC'
Goran_pattern = 'CCAABB'

Adrian_count = 0
Bruno_count = 0
Goran_count = 0

if question_num != len(given_answer):
    exit()

for i in range(question_num):
    if given_answer[i] == Adrian_pattern[i % len(Adrian_pattern)]:
        Adrian_count += 1

for i in range(question_num):
    if given_answer[i] == Bruno_pattern[i % len(Bruno_pattern)]:
        Bruno_count += 1

for i in range(question_num):
    if given_answer[i] == Goran_pattern[i % len(Goran_pattern)]:
        Goran_count += 1

#최대 정답 값을 구함
max_count = max(Adrian_count, Bruno_count, Goran_count)
print(max_count)

#최대 정답 값을 맞춘 사람을 알파벳 순서로 출력
winners = []
if Adrian_count == max_count:
    winners.append('Adrian')
if Bruno_count == max_count:
    winners.append('Bruno')
if Goran_count == max_count:
    winners.append('Goran')

for winner in winners:
    print(winner)

