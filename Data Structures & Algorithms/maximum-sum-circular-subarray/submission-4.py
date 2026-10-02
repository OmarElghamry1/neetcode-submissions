class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int: 
        
        # Global Max, Global Min
        gmax, gmin = nums[0], nums[0]

        curMax, curMin = 0, 0
        total = 0

        for n in nums: 
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)

            gmax = max(curMax, gmax)
            gmin = min(curMin, gmin)
            total += n
        
        # in case array is all negative. 
        if gmax < 0: 
            return gmax
        else: 
            return max(total - gmin, gmax)








   

        