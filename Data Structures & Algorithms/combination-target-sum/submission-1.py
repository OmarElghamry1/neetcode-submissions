class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        res = []

        cur_sum = []

        def _combine(i, total): 
            if total >= target or i >= len(nums): 
                if total == target: 
                    res.append(cur_sum.copy())
                    return 
                else: 
                    return 

            cur_sum.append(nums[i])
            _combine(i, total+nums[i])

            cur_sum.pop()
            _combine(i+1, total)
        
        _combine(0, total=0)
        
        return res

                