# 입력받기
n = int(input())
lines = [input().strip() for _ in range(n)]

# 결과 출력
for line in lines:
    encoded = []
    i = 0
    while i < len(line):
        count = 1
        while i + 1 < len(line) and line[i] == line[i + 1]:
            count += 1
            i += 1
        encoded.append(f"{count} {line[i]}")
        i += 1
    print(" ".join(encoded))
