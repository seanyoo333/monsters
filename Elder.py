
#첫번째 소유자, 대문자로 표시한다
current_owner = input()

# 1 <= N <= 100
num_of_duals = int(input())

# 결투에 따른 완드의 소유자들
owners_set = {current_owner}

# 결투 처리, Z1(새 도전자가) Z2(원소유자가)를 이김
for _ in range(num_of_duals):
    Z1, Z2 = input().strip().split()
    if Z2 == current_owner:
        current_owner = Z1
        owners_set.add(current_owner)

print(current_owner)
print(len(owners_set))

