# year 2015 only
t_month = int(input('enter only between 1 and 12: '))
t_day = int(input('enter only between 1 and 31: '))

if t_month == 2 and t_day == 18 :
    print("Special")
elif 1 == t_month :
    print("Before")
elif 2 == t_month and t_day < 18 :
    print("Before")
elif 2 < t_month :
    print("After")
elif 2 == t_month and t_day > 18 :
    print("After")


