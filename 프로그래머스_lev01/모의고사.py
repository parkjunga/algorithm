'''


'''
import operator


def solution(answers):
    answer = []
    count = 0
    test = [[1, 2, 3, 4, 5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    le = {}
    score = []
    for j in range(len(test)):
        count = 0
        for i in range(len(answers)):
            if test[j][i] == answers[i]:
                count += 1
                #print(test[j][i],count)
        score.append(count)
    #print(score)

    for p,s in enumerate(score):
        if s == max(score):
            answer.append(p+1)
    #print(answer)
        # if count > 0:
        #     le[j+1] = count
    # if len(le) > 1:
    #     le = sorted(le.items(), key=operator.itemgetter(0))
    #     for i in range(len(le)):
    #         if le[i][1] > 0:
    #             answer.append(le[i][0])
    # else:
    #     answer.append(list(le)[0])
    return answer

answers = [1,3,2,4,2]
ans = solution(answers)
print(ans)