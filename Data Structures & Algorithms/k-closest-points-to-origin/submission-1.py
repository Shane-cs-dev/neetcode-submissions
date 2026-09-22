class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = [(-((x*x + y*y)**0.5), [x, y]) for x, y in points]

        heapq.heapify(dis)

        while len(dis) > k:
            heapq.heappop(dis)
        
        return [point for dis, point in dis]