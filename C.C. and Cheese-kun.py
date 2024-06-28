# 1<= width <= 3
# 0 <= cheesiness < = 100

width = int(input())

cheesiness = int(input())
satisfied_1 = 'absolutely'
satisfied_2 = 'fairly'
satisfied_3 = 'very'

if width == 3 and cheesiness >= 95 :
    print("C.C. is " + satisfied_1 + ' satisfied with her pizza.')
elif width == 1 and cheesiness <= 50 :
    print("C.C. is " + satisfied_2 + ' satisfied with her pizza.')
else :
    print("C.C. is " + satisfied_3 + ' satisfied with her pizza.')
