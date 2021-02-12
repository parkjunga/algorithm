'''
문제 접근법
1. 그리드 알고리즘 사용
2. 핵심은 빨리 끝나느 회의 순서대로 정렬해야 한다.
3. 현재 상황에서 최선의선택(가장 회의가 빨리 끝나는)

주의사항
1. 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에
다음 회의가 시작될 수 있다. 회의의 시작과 끝나느 시간이 같을 수 있다.
이 경우 시작하자마자 끝난다고 생각하면됨.

'''

def solution(arr):
    cnt = 0
    endTime = 0
    for i in range(len(arr)):
        if endTime <= arr[i][0]:
            endTime = arr[i][1]
            cnt += 1
    return cnt

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

# x[1] 끝나느 시간이 가장 빠른 순
# x[0] 시작하는 시간의 오름차순
# key에 2개의 인자를 주면 인자의 순서대로 정렬

arr.sort(key=lambda x: (x[1], x[0]))
print(solution(arr))