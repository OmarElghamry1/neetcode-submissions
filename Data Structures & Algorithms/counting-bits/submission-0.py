class Solution:
    def countBits(self, n: int) -> List[int]:

        def count_bits(n): 
            count = 0
            while n > 0: 
                if n & 1 == 1: 
                    count += 1
                n = n >> 1
            return count
        
        n_bits = []

        for i in range(n + 1): 
            n_bits.append(count_bits(i))
        

        return n_bits
        


        
        