class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        curSum = sum(arr[:k])
        res = 0

        if (curSum / k) >= threshold: 
                res += 1

        for i in range(k, len(arr)): 

            curSum -= arr[i - k]
            curSum += arr[i]

            if (curSum / k) >= threshold: 
                res += 1
            
       
        return res
        