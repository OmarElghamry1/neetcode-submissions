from heapq import heappush, heappop, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        # O(n)
        for x, y in points:
            dist = x**2 + y**2
            heap.append((dist, [x, y]))

        heapify(heap)  # O(n)

        res = []
        # O(k logn)
        for _ in range(k): 
            res.append(heappop(heap)[1])

        return res




        

        

        

        