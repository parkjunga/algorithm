import math


def solution(progresses, speeds):
    answer = []
    check = [ math.ceil((100 - x)/y) for x, y in zip(progresses, speeds)]
    while len(check) > 0:
        # 자기자신 포함
        cnt = 1
        a = check.pop(0)
        check1 = check.copy()
        for i in range(len(check)):
            print(a, check[i])
            if a >= check[i]:
                cnt += 1
                # 계산한 내역 빼주기
                check1.pop(0)
            else:
                break
        answer.append(cnt)
        check = check1.copy()
    return answer
        # stack = []
    # count = 0
    # ceil = math.ceil(100-progress[0]/speeds[0])
    # for i in range(1,len(progress)):
    #     if ceil <= math.ceil(100-progress[i]/speeds[i]):
    #         count += 1
    #         stack.append(math.ceil(100-progress[i]/speeds[i]))
    #     else:
    #         answer.append(count)
    #         count = 1
    #         stack.append(math.ceil(100-progress[i]/speeds[i]))
    #         answer.append(count)



progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

ans = solution(progresses, speeds)
print(ans)