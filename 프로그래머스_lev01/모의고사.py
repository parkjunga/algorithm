'''
수포자는 수학을 포기한 사람의 준말입니다.

수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5,
                     1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5,
                     2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5,
                     3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...


1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

1. 이 문제는 가장 많은 문제를 맞힌 사람만 배열에 담는것
2. 똑같을때만 다 출력
'''


def solution(answers):
    mx = {}

    qna1 = [1, 2, 3, 4, 5] # 2
    qna2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 1
    qna3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] #1
    count = [0,0,0]
    answer = []
    for i in range(len(answers)):
        if qna1[i%5] == answers[i]:
            count[0] += 1
        if qna2[i%8] == answers[i]:
            count[1] += 1
        if qna3[i%10] == answers[i]:
            count[2] += 1


    if count[0] > 0:
        mx[1]= count[0]
    if count[1] > 0:
        mx[2] = count[1]
    if count[2] > 0:
        mx[3] = count[2]

    mx = sorted(mx.items(), key=lambda x: x[1], reverse=True)
    answer.append(mx[0][0])
    m = mx[0][1]
    for i in range(1,len(mx)):
        if m == mx[i][1]: # 맨앞 값이랑 같으면
            answer.append(mx[i][0])

    if len(answer) == 0:
        answer = [1,2,3]
#    answer = list(filter(lambda x: x != 0, answer))

    return answer

answers =  [1,2,3,4,5,3,4,5,6]
ans = solution(answers)
print(ans)