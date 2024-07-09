# 0 < line < 10000, followed by N lines
line_of_text = int(input())
if not 0 < line_of_text < 100:
    exit()

# 1 <= each line char < 100
sentences = []

for i in range(line_of_text):
    while True:
        line = input('문장을 입력하세요: ')
        char_count = len(line)
        if 1 < char_count < 100:
            sentences.append(line)
            break
        else:
            print('문장의 글자는 1개 초가 100개 미만이어야 합니다. 다시 입력해 주세요')

"""3
Oh it is monday
i feel tired
but I have new way to overcome it. """
English_count = 0
French_count = 0

for sentence in sentences:
    for char in sentence:
        if char == 't' or char == 'T':
            English_count += 1
        elif char == 's' or char == 'S':
            French_count += 1

if English_count > French_count:
    language = 'English'
elif English_count < French_count:
    language = 'French'
elif English_count == French_count:
    language = 'French'

print(language)
