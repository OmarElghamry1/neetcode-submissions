class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res, subset = [], []

        def _subset(index): #helper function 
            if index == len(nums): 
                res.append(subset.copy()) # make another reference
                return 

            subset.append(nums[index])
            _subset(index+1) #left branch
            
            subset.pop()
            _subset(index+1) # right branch

            return res
            
        
        _subset(0)

        return res