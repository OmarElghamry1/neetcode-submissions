class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l =1 
        for r in range(len(nums)): 
            if nums[r] == nums[l-1]: 
                continue
            nums[l] = nums[r]
            l+=1
        return l
