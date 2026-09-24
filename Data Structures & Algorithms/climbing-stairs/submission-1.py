class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1: 
            return n
        

        cache = [0, 1]
        for _ in range(n + 1): 
            tmp = cache[1]
            cache[1] = cache[0] + cache[1]
            cache[0] = tmp


        return cache[0]




            


            
                
            
            
    

        
            