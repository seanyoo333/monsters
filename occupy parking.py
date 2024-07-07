# 주차장 수는 1<= N <= 100

parking_lot_num = int(input())
if not 1 <= parking_lot_num <= 100:
    exit('주차장 수를 범위안에서 입력하세요')

# 주차된 공간은 'C', 빈 공간은 '.'
occupied_yesterday = input()
if len(occupied_yesterday) != parking_lot_num :
    exit('주차장 수 내에서 입력하세요')

occupied_today = input()
if len(occupied_today) != parking_lot_num :
    exit('주차장 수 내에서 입력하세요')

occupied = 0
for i in range(parking_lot_num) :
    if occupied_yesterday[i] == 'C' and occupied_today[i] == 'C' :
       occupied = occupied + 1

print(occupied)
