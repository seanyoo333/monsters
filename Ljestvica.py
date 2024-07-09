""" 음계의 수는 2 <= sequence <= 100
음계의 종류 A, B, C, D, E, F, G, I
I는 음계 사이에 중복사용이, 맨 앞, 맨뒤에 올수 없다
"""
sequence = input()

measures = sequence.split('|')

main_tone_A_minor = {'A', 'D', 'E'}
main_tone_C_major = {'C', 'F', 'G'}

count_A_minor = 0
count_C_major = 0

for measure in measures:
    if measure:
        first_tone = measure[0]
        if first_tone in main_tone_A_minor:
            count_A_minor += 1
        if first_tone in main_tone_C_major:
            count_C_major += 1


if count_A_minor > count_C_major:
    print("A-mol")
elif count_C_major > count_A_minor:
    print("C-dur")
else:
    last_tone = sequence[-1]
    if last_tone == 'A':
        print("A-mol")
    elif last_tone == 'C':
        print("C-dur")

