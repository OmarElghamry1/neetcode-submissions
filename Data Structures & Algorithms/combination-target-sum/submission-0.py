class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        res = []

        cur_sum = []

        def _combine(i): 
            if sum(cur_sum) >= target or i >= len(nums): 
                if sum(cur_sum) == target: 
                    res.append(cur_sum.copy())
                    return 
                else: 
                    return 

            cur_sum.append(nums[i])
            _combine(i)

            cur_sum.pop()
            _combine(i+1)
        
        _combine(0)
        
        return res

                