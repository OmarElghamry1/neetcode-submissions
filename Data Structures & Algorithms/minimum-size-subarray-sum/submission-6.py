class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_len = float('inf')
        curr_sum = 0

        
        for R in range(len(nums)): 
            curr_sum += nums[R] 

            while curr_sum >= target: 
                min_len = min(min_len, R - L + 1)
                curr_sum -= nums[L]
                L += 1
        
        return 0 if min_len == float('inf') else min_len
