import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    heapp = []
    for num in heap:
        heapq.heappush(heapp, num)
    
    ans = []
    while (len(heapp) != 0):
        ans.append(heapq.heappop(heapp))

    return ans



# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
