class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return nums[0]

        amt = [0, 0]
        amt[0] = nums[0]
        amt[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)): 
            tmp = amt[1]
            amt[1] = max(amt[1], nums[i] + amt[0])
            amt[0] = tmp
        
        return amt[1]



    
