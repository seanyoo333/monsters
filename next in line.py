# 0<= Y <= 50
Y = int(input())

# Y <= M < 50
while True :
    M = int(input())
    if Y <= M < 50:
        break
    print("Y와 같거나 큰 수를 입력하세요")

O = M + (M-Y)
print(O)