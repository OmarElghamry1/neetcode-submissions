class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        char_set = set()
        res = 1
        
        if not s: 
            return 0


        for R in range(len(s)): 
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1

            res = max(res, R - L + 1)
            char_set.add(s[R])
            
            
        return res

   

            
            

        