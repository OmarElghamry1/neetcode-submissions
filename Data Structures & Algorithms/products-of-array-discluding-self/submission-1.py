class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = []

        prefix = 1
        for n in nums: 
            arr.append(prefix)
            prefix *= n
        
        postfix = 1
        for j in range(len(nums) - 1, -1, -1): 
            arr[j] *= postfix
            postfix *= nums[j]
        
        return arr
