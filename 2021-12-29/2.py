import heapq

heap = []

heapq.heappush(heap, -1)
heapq.heappush(heap, -32)
heapq.heappush(heap, -55)
heapq.heappush(heap, -8)
heapq.heappush(heap, -454)
while heap:
    print(-heapq.heappop(heap))