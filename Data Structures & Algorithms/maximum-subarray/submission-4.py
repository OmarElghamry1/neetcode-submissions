class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        

        for n in nums: 
            curSum = max(n, n + curSum)
            maxSum = max(maxSum, curSum)
            
        

        return maxSum 
        
        