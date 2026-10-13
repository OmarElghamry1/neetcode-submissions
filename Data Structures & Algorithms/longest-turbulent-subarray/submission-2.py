class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res, L = 1, 0
        prev = ""
        R = 1
        while R < len(arr): 
            if arr[R - 1] < arr[R] and prev != "<": 
                res = max(res, R - L + 1)
                R += 1
                prev = "<"
            
            elif arr[R - 1] > arr[R] and prev != ">": 
                res = max(res, R - L + 1)
                R += 1
                prev = ">"
            
            else: 
                R = R + 1 if arr[R - 1] == arr[R] else R
                L = R - 1
                prev = ""
        
        return res

        