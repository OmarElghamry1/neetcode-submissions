class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for n in nums: 
            total += n
            prefix.append(total)

        
        for i in range(len(nums)): 
            leftsum = prefix[i - 1] if i > 0 else 0
            rightsum = total - prefix[i]

            if leftsum == rightsum: 
                return i
            

        return -1


            

   


