import heapq
def solution(scoville, K):
    answer = 0

    while K >= min(scoville):
        scoville.sort()
        tmp = scoville[0] + (scoville[1] * 2 )
        scoville = scoville[2:]
        scoville.insert(0,tmp)
        answer += 1
    #print(scoville)
    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7
ans = solution(scoville,k)
print(ans)