class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp1 = nums[i]
            for j in range(i+1, len(nums)):
                temp2 = nums[j]
                if (temp1 + temp2) == target: 
                    return [i, j]

        