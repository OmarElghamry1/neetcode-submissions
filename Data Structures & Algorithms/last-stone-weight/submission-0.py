import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) > 1: 
            w1 = heapq._heappop_max(stones)
            w2 = heapq._heappop_max(stones)

            if w1 > w2: 
                w1 = w1 - w2
                heapq._heappush_max(stones, w1)
            elif w2 > w1: 
                w2 = w2-w1
                heapq._heappush_max(stones, w2)

        return stones[0] if len(stones) == 1 else 0