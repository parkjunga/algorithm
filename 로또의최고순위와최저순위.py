def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    win_nums_count = 0
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero_count += 1
        else:
            if lottos[i] in win_nums:
                win_nums_count += 1
    lottosNum = [6,5,4,3,2,1]

    win = lottosNum[zero_count+win_nums_count-1]
    if win_nums_count == 0:
        loser = lottosNum[win_nums_count]
    else:
        loser =lottosNum[win_nums_count-1]

    if win_nums_count == 0 and zero_count == 0: # 모두 다를경우를 고려
        win = lottosNum[0]
        loser = lottosNum[0]

    answer.append(win)
    answer.append(loser)
    return answer


lottos = [1, 2, 6, 23, 43, 29]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos,win_nums))