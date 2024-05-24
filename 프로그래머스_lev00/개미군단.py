def solution(hp):
    answer = 0
    top = 5
    middle = 3
    row = 1
    answer = hp // top
    hp = hp % top
    while hp > 0:
        if hp % middle == 0 and hp >= middle:
            answer += hp // middle
            hp = hp % middle
        elif hp >= row:
            answer += row
            hp = hp - row
        else:
            answer += hp // row


    return answer



hp = 28
answer = solution(hp)
print(answer)