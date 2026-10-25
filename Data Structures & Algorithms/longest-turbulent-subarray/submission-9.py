class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L = 0
        max_len = 1
        prev = ""
        R = 1

        while R < len(arr): 
            if arr[R - 1] < arr[R] and prev != "<":
                max_len = max(max_len, R - L + 1)
                prev = "<"
                R += 1
            elif arr[R - 1] > arr[R] and prev != ">":
                max_len = max(max_len, R - L + 1)
                prev = ">"
                R += 1
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1
                prev = ""


        return max_len