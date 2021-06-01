def solution(phone_book):
    answer = True
    # 거꾸로일때 경우를 고려한다.
    phone_book.sort()

    # for문을 1번으로 줄였다.
    for i in range(len(phone_book)): # 0,1,2
        if i+1 < len(phone_book):
            if phone_book[i+1].startswith(phone_book[i]):
                answer = False
                return answer

    return answer

phone_book =["123","456","789"]
print(solution(phone_book))