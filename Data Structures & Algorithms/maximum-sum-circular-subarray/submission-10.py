class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        Max, Min = nums[0], nums[0]
        total = 0

        curMax, curMin = 0, 0

        for n in nums: 
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            Max = max(curMax, Max)
            Min = min(curMin, Min)
        
        if Max < 0: 
            return Max
        else: 
            return max(total - Min, Max)


        
        
        








   

        