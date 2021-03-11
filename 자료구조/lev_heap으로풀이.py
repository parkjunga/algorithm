import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville) # 힙구조로 바꿈
    while True:
        first = hq.heappop(scoville) # 가장 작은값
        if first >= K: # K보다 클때
            break
        if len(scoville) == 0:  # 만약 길이가 0일때는 -1
            return -1
        second = hq.heappop(scoville) # 두번째로 작은값 출력
        hq.heappush(scoville, first + second * 2) 
        answer += 1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
ans = solution(scoville,k)
print(ans)