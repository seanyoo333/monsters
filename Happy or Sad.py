# 1 <= characters <= 255
feel_today = input("오늘의 기분을 :-) 또는 :-( 와 함께 표현 하세요" )

happy_count = feel_today.count(:-))
sad_count = feel_today.count(:-()

if happy_count == 0 and sad_count == 0 :
    print("none")
elif happy_count == sad_count :
    print)("unsure")
elif happy_count > sad_count :
    print("happy")
elif happy_count < sad_count :
    print("sad")

print(feel_today)
