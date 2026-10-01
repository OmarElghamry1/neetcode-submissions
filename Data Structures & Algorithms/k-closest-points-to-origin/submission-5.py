from heapq import heappush, heappop, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        dist = []
        for x, y in points: 
            dist.append((x**2 + y **2, x, y))
        
        heapify(dist)

        res = []
        for i in range(k): 
            d, x, y = heappop(dist)
            res.append([x, y])

        return res




       


        

        

        

        