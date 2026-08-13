class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for i in nums:
            if i not in num_dict:
                num_dict[i] = i
            else:
                num_dict[i] += i
                return True
    
        return False

    
        
         