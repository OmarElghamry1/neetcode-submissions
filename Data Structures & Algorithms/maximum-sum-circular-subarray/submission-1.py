class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

         n = len(nums)
         maxSum = nums[0]
         for start in range(n):
            curSum = 0
            for length in range(n):
                curSum += nums[(start + length) % n]
                maxSum = max(maxSum, curSum)
         return maxSum

   

        