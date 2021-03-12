from sys import stdin
import heapq as hq

n = int(stdin.readline().strip())
heap = []
for _ in range(n):
    x = int(stdin.readline().strip())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap,x)


