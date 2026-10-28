class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        maxSum, minSum = nums[0], nums[0]
        curSum, curMin = 0, 0
        total = 0

        for n in nums: 
            curSum = max(n, n + curSum)
            curMin = min(n, n + curMin)
            total += n
            maxSum = max(curSum, maxSum)
            minSum = min(curMin, minSum)
        
        return maxSum if maxSum < 0 else max(total - minSum, maxSum)
        