# only A, B, C at most 50 characters
swap_pattern = input()
if not all(c in 'ABC' for c in swap_pattern):
    exit('ABC 이외의 글자가 입력 되었음')

if len(swap_pattern) > 50 :
    exit('입력글자 수가 50을 초과했음')

ball_location = 1

for swap in swap_pattern :
    if swap == 'A' and ball_location == 1 :
        ball_location = 2
    elif swap == 'A' and ball_location == 2 :
        ball_location = 1
    elif swap == 'A' and ball_location == 3 :
        ball_location = 3
    elif swap == 'B' and ball_location == 1 :
        ball_location = 1
    elif swap == 'B' and ball_location == 2 :
        ball_location = 3
    elif swap == 'B' and ball_location == 3 :
        ball_location = 2
    elif swap == 'C' and ball_location == 1 :
        ball_location = 3
    elif swap == 'C' and ball_location == 2 :
        ball_location = 2
    elif swap == 'C' and ball_location == 3 :
        ball_location = 1
print(ball_location)



