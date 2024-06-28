# 0<= Y <= 50
Y = int(input())

# Y <= M < 50
M = int(input())
if M < Y :
    print("Y와 같거나 큰 수를 입력하세요")

O = M + (M-Y)
print(O)
