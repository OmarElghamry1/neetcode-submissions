class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums: 
            return 0
        
        if len(nums) == 1: 
            return nums[0]
        
        rob = [0, 0]
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = rob[1]
            rob[1] = max(rob[1], rob[0]+nums[i])
            rob[0] = tmp
        
        return rob[1]
