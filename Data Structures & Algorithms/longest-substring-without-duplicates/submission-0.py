class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        L = 0
        window = set()
        maxx = 0
        cur = 0

        for R in range(len(s)): 
            
            while s[R] in window: 
                window.remove(s[L])
                L += 1
    
            cur = 0
            window.add(s[R])
            maxx = max(maxx, len(window))

        return maxx
            
                
            

            
            

        