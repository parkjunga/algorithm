# 최대힙
import heapq as hq
from sys import stdin
n = int(stdin.readline().strip())
heap = []
for _ in range(n):
    x = int(stdin.readline().strip())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(hq.heappop(heap)*(-1)) # 맥스일경우 값을 -로 바꾸면됨
    else:
        hq.heappush(heap,-x)