class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curMax = 0

        for n in nums: 
            curMax = max(n, curMax + n)
            maxSum = max(maxSum, curMax)
            
        return maxSum
        
        
        