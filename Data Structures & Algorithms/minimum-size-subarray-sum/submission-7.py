class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        L = 0
        run_sum = 0
        min_len = float('inf')
        

        for R in range(len(nums)): 
            run_sum += nums[R]
            
            while run_sum >= target: 
                min_len = min(R - L + 1, min_len)
                run_sum -= nums[L]
                L += 1
            
            
        return 0 if min_len == float('inf') else min_len
                 








        