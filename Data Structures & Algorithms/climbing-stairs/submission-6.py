class Solution:
    def climbStairs(self, n: int) -> int:

        prev, cur = 1, 1

        for i in range(1, n): 
            tmp = cur
            cur = cur + prev
            prev = tmp
        
        return cur


        