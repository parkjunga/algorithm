
def solution(answers):
    answer = []

    #찍는 방식의 패턴
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]

    # 점수판
    scores = [0,0,0]

    for index in range(len(answers)):
        if answer_1[index % 5] == answers[index]:
            scores[0] += 1

        if answer_2[index % 8] == answers[index]:
            scores[1] += 1

        if answer_3[index % 10] == answers[index]:
            scores[2] += 1
    print(scores)

    test = []

solution([1,2,3,4,5])