class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
            L = 0
            win = set()
            res = 0 # longest subtring

            for R in range(len(s)):

                while s[R] in win: 
                    win.remove(s[L])
                    L += 1
                    
                win.add(s[R])

                res = max(R - L + 1, res)
        
            return res



                

        