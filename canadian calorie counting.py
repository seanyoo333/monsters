# menu only 1~4
burger_choice = int(input())
if burger_choice == 1:
    burger_choice = 461
elif burger_choice == 2:
    burger_choice = 431
elif burger_choice == 3:
    burger_choice = 420
elif burger_choice == 4:
    burger_choice = 0
else :
    print('enter only 1 to 4')


side_choice = int(input())
if side_choice  == 1:
    side_choice = 100
elif side_choice == 2:
    side_choice = 57
elif side_choice == 3:
    side_choice = 70
elif side_choice == 4:
    side_choice = 0
else :
    print('enter only 1 to 4')

drink_choice = int(input())
if drink_choice == 1:
    drink_choice =130
elif drink_choice == 2:
    drink_choice = 160
elif drink_choice == 3:
    drink_choice = 118
elif drink_choice == 4:
    drink_choice = 0
else :
    print('enter only 1 to 4')

dessert_choice = int(input())
if dessert_choice == 1:
    dessert_choice = 167
elif dessert_choice == 2:
    dessert_choice = 266
elif dessert_choice == 3:
    dessert_choice = 75
elif dessert_choice == 4:
    dessert_choice = 0
else :
    print('enter only 1 to 4')


total_calorie = burger_choice + side_choice + drink_choice + dessert_choice
print(f"Your total Calorie count is {total_calorie}.")
