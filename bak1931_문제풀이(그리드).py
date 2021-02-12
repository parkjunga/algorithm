def solution(InputArr):
    answer = 0
    endTime = 0
    for i in range(len(InputArr)):
        if endTime <= InputArr[i][0]:
            endTime = InputArr[i][1]
            answer += 1
    return answer


N = int(input())
InputArr = []

for i in range(N):
    A, B = map(int, input().split())
    InputArr.append([A, B])

# 이 key=lambda x: (x[1], x[0]) 코드는
# 전체 리스트를 x[1] 즉 끝나는 시간대로 정렬을 하고 그 안에서 다시 x[0] 시작 시간으로 정렬시킨는 코드이다.
InputArr.sort(key=lambda x: (x[1], x[0]))

# 파이썬 리스트는 sort()라는 메소드를 가지고 이 메소드는 리스트를 정렬된 상태로 변경
# key 매개변수
# 객체의 데이터중에서 특정한 데이터를 기준으로 정렬하기 위해 key 매개변수로 정렬을 하기 전에 각 요소에 대하여 적용되는 함수를 지정할 수 있다.

print(InputArr)
print(solution(InputArr))