class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        count = {}
        res = 0

        for R in range(len(s)): 
            count[s[R]] = 1 + count.get(s[R], 0)

            max_char = max(count.values())

            if (R - L + 1 - max_char) > k: 
                count[s[L]] -= 1
                L += 1
            
            res = max(res, R - L + 1)
        
        return res
            
            
            


        

        