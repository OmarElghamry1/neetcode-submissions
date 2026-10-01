from heapq import heappush, heappop, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        # O(n)
        for x, y in points: 
            dist.append((x**2 + y **2, x, y))
        
        # O(n)
        heapify(dist)

        res = []
        # O(klogn)
        for i in range(k): 
            d, x, y = heappop(dist)
            res.append([x, y])

        return res #O(n + klogn) instead of O(n + nlogn)




       


        

        

        

        