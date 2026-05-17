import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    new_heap = []
    for i in heap:
        heapq.heappush(new_heap, i)
    heapq.heappush(new_heap, value)
    return new_heap[0]



# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
