# 입력값은 100이하의 정수

a_bowl_weight = int(input())
b_bowl_weight = int(input())
c_bowl_weight = int(input())

if c_bowl_weight > a_bowl_weight > b_bowl_weight or b_bowl_weight > a_bowl_weight > c_bowl_weight :
    middle = a_bowl_weight
elif c_bowl_weight > b_bowl_weight > a_bowl_weight or a_bowl_weight > b_bowl_weight > c_bowl_weight :
    middle = b_bowl_weight
elif a_bowl_weight > c_bowl_weight > b_bowl_weight or b_bowl_weight > c_bowl_weight > a_bowl_weight :
    middle = c_bowl_weight

print(middle)

