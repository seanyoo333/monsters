# 1 <= N <= 100000
honi_block = input()

H_block = 0
O_block = 0
N_block = 0
I_block = 0

for i in honi_block:
    if i == 'H':
        H_block += 1
    elif i == 'O':
        O_block += 1
    elif i == 'N':
        N_block += 1
    elif i == 'I':
        I_block += 1


count_honi = min(H_block, O_block, N_block, I_block)
print(count_honi)


honi_block = input()

H_count = 0
O_count = 0
N_count = 0
I_count = 0
count_honi = 0

for i in honi_block:
    if i == 'H' and H_count == count_honi:
        H_count += 1
    elif i == 'O' and H_count > O_count:
        O_count += 1
    elif i == 'N' and O_count > N_count:
        N_count += 1
    elif i == 'I' and N_count > I_count:
        I_count += 1
        count_honi += 1

print(count_honi)