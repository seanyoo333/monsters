# 질문 수는 0 < N < 10000
num_questions = int(input())
if not 0< num_questions < 10000:
    exit()

student_answer = []
correct_answer = []

for _ in range(num_questions):
    student_answer.append(input())

for _ in range(num_questions):
    correct_answer.append(input())

correct_count = 0

for i in range(num_questions):
    if student_answer[i] == correct_answer[i]:
        correct_count += 1

print(correct_count)
