from heapq import heapify_max, heappush_max, heappop_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapify_max(stones)

        while len(stones) > 1: 
            first = heappop_max(stones)
            second = heappop_max(stones)

            if first > second: 
                # first can be only bigger or equal to second
                heappush_max(stones, first-second)

            
        return stones[0] if len(stones) > 0 else 0








        

            
            



