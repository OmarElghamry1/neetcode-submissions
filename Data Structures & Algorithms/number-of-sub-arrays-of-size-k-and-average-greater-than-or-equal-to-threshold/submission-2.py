class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L = 0
        cur_sum = 0
        count = 0

        for R in range(len(arr)): 
            cur_sum += arr[R]
            if (R - L + 1) == k: 
                if (cur_sum / k) >= threshold: 
                    count += 1
                cur_sum -= arr[L]
                L+= 1
        return count
                
            
            


   
        