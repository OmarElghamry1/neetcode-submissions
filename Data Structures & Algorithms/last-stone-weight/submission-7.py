from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapify_max(stones)
        while len(stones) > 1: 
            fst = heappop_max(stones)
            sec = heappop_max(stones)

            if (fst > sec): 
                heappush_max(stones, (fst-sec))
        
        stones.append(0)
        return stones[0]




        

            
            



