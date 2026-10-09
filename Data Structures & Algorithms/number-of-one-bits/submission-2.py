class Solution:
    def hammingWeight(self, n: int) -> int:
        
        nbits = 0
        while n > 0: 
            nbits += 1 & n
            n = n // 2
        
        return nbits
        
 