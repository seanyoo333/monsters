while True:
    word = input().strip()
    if word == "quit!":
        break

    # 단어의 길이가 4자 이상인지 확인
    if len(word) > 4:
        # 단어의 끝이 "or"이고, 그 앞 문자가 자음인지 확인
        if word[-2:] == "or" and word[-3].lower() not in "aeiouy":
            # "or"을 "our"로 변환
            word = word[:-2] + "our"

    # 결과 출력
    print(word)
    