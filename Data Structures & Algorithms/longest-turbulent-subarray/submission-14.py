class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        prev = ""
        R = 1
        res = 1

        while R < len(arr): 

            if arr[R - 1] < arr[R] and prev != "<": 
                res = max(R - L + 1, res)
                R += 1
                prev = "<"
            
            elif arr[R - 1] > arr[R] and prev != ">":
                res = max(R - L + 1, res)
                R += 1
                prev = ">"
            
            else: 
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1
                prev = ""
        
        return res



            


        