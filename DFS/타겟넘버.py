'''
cnt 는 number를 몇번했는지 확인
result 는 tmp값 1로 타겟값까지 되는지 확인
재귀
'''


answer = 0


def DFS(cnt, result, target, numbers):
    n = len(numbers)
    if cnt == n: # 갯수만큼 돌렸으면
        if result == target: # 결과값이 target이랑 같으면
            global answer
            answer += 1
        return
    else:
        DFS(cnt + 1, result + numbers[cnt], target, numbers)
        DFS(cnt + 1, result - numbers[cnt], target, numbers)


def solution(numbers, target):
    global answer
    DFS(0, 0, target, numbers)
    return answer


numbers = [1,1,1,1,1]
target = 3
print(solution(numbers,target))