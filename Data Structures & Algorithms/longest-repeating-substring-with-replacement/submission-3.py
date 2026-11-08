class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        win = {}
        res = 0
        

        for R in range(len(s)): 
            win[s[R]] = 1 + win.get(s[R], 0)
            max_char = max(win.values())

            if (R - L + 1) - max_char > k: 
                win[s[L]] -= 1
                L += 1

            
            res = max(res, R - L + 1)
        
        return res




            



        