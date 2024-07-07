# 8<= password <=12
password = str(input())

if not 8 <= len(password) <= 12:
    exit()

# 3, 2, 1
lowercase = 0
uppercase = 0
digit = 0

for char in password:
    if char.islower():
        lowercase += 1
    elif char.isupper():
        uppercase += 1
    elif char.isdigit():
        digit += 1

if lowercase >= 3 and uppercase >= 2 and digit >= 1:
    print('Valid')
else:
    print('Invalid')
