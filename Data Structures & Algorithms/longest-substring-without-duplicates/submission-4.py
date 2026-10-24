class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R = 0, 0
        win = set()
        longest = 0

        while R < len(s): 
            while s[R] in win: 
                win.remove(s[L])
                L += 1
                
            win.add(s[R])
            longest = max(longest, R - L + 1)
            R += 1
        
        return longest

        