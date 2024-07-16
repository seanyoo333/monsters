#1 <= b <= 4
button_num = 0

# 1<= n < = 10
num_timepressed = 0

playlist = 'ABCDE'

while button_num != 4:
    button_num = int(input())
    button_numpressed = int(input())
    for i in range(button_numpressed):
        if button_num == 1:
            playlist = playlist[1:] + playlist[0]

        elif button_num == 2:
            playlist = playlist[4] + playlist[0:4]

        elif button_num == 3:
            playlist = playlist[1] + playlist[0] + playlist[2:]


output = ''
for song in playlist:
    output = output + song + ' '

print(output[:-1])