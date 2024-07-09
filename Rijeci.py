
# 버튼을 누른 수는 1<= K <= 45
num_pressed_button = int(input())
if not 1 <= num_pressed_button <= 45:
    exit()

count_A = 1
count_B = 0

for _ in range(num_pressed_button):
    new_count_A = count_B
    new_count_B =count_B + count_A
    count_A = new_count_A
    count_B = new_count_B

print(count_A, count_B)





