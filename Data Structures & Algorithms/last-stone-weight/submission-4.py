from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapify_max(stones)


        while len(stones) > 1: 

            first = heappop_max(stones)
            second = heappop_max(stones)

            if first > second: 
                heappush_max(stones, (first-second))
        

        stones.append(0)
        return stones[0]
        






        

            
            



