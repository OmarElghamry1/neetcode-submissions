class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t): 
            for i in s: 
                if i in t: 
                    t = t.replace(i, '', 1)
                else: 
                    return False
            if not t: 
                return True
            else: 
                return False
        else: 
            return False 
        