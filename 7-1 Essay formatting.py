input_file = open('word.in', 'r')
output_file = open('word.out', 'w')

#n = 한 줄에 단어수 1 < n < 100
#k = 한 줄에 가능 문자수 1 < k < 80
lst = input_file.readline().split()
n = int(lst[0])
k = int(lst[1])
words = input_file.readline().split()

line = ''
chars_on_line = 0

for word in words:
    if chars_on_line + len(word) <= k:
        line = line + word + ''
        chars_on_line = chars_on_line + len(word)

    else:
        output_file.write(line[:-1] + '\n')
        line = word + ''
        chars_on_line = len(word)

output_file.write(line[:-1] + '\n')

input_file.close()
output_file.close()


