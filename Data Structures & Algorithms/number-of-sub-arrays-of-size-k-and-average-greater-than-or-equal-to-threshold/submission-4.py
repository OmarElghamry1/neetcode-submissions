class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        arr_sum = sum(arr[:k])
        res = 0
        if arr_sum >= k * threshold: 
            res += 1
        
        for i in range(k, len(arr)): 
            arr_sum -= arr[i - k]
            arr_sum += arr[i]
            if arr_sum >= k * threshold: 
                res += 1
        
        return res



        