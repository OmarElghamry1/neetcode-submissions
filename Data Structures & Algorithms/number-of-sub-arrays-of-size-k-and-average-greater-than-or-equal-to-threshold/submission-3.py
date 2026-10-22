class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        avg = sum(arr[:k])
        count = 0

        if avg >= k * threshold: 
            count += 1
        
        for R in range(k, len(arr)): 
            
            avg += arr[R]
            avg -= arr[R - k]
            
            if avg >= k * threshold: 
                count += 1
            

        return count
        