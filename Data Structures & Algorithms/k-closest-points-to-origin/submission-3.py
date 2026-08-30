from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        for x, y in points: 
            ## euclidean distance
            dist = (x**2) + (y**2)

            heappush(heap, (dist, [x, y]))
        res = []
        for i in range(k): 
            res.append(heappop(heap)[1])

        return res




        

        

        

        