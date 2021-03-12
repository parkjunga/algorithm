import heapq as hq
def solution(scoville, K):
    answer = 0
    hq.heapify(scoville) # 힙구조로 바뀜
    #print(hq.heappop(scoville)) # 최소값 뽑고
    while True: # while 문을 돌리면서
        first = hq.heappop(scoville)
        if K > first:
            tmp = first + hq.heappop(scoville) * 2
            hq.heappush(scoville,tmp)
            answer += 1
        else:
            break
        if len(scoville) == 0:
            return -1
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
ans = solution(scoville,k)
print(ans)