import heapq
import sys

N = int(input())

queue = []
for _ in range(N):
    num = int(sys.stdin.readline())

    if not num:
        if not queue:
            print(0)
        else:
            print(heapq.heappop(queue))

    else:
        heapq.heappush(queue, num)