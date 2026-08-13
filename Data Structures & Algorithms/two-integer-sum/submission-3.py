class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}  # Dictionary to store the number and its index
    
        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_to_index:
                return [num_to_index[difference], i]
            num_to_index[num] = i
    
        return []  # In case no solution is found (though the problem guarantees one)
        
        
        """
        Solution 1
        for i in range(len(nums)):
            temp1 = nums[i]
            for j in range(i+1, len(nums)):
                temp2 = nums[j]
                if (temp1 + temp2) == target: 
                    return [i, j]
        """

        