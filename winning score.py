# a팀 점수
a_three_p = int(input())
a_two_p = int(input())
a_one_p = int(input())

#b팀 점수
b_three_p = int(input())
b_two_p = int(input())
b_one_p = int(input())

apple_total = a_three_p * 3 + a_two_p * 2 + a_one_p
banana_total = b_three_p * 3 + b_two_p * 2 + b_one_p

if apple_total > banana_total :
    print('A')
elif apple_total < banana_total :
    print("B")
else :
    print("T")
