class Solution:
    def climbStairs(self, n: int) -> int:

        cache = [1, 1]

        for i in range(n - 1): 
            tmp = cache[1]
            cache[1] = cache[0] + cache[1]
            cache[0] = tmp
        
        return cache[1]
        
   
        

            


            
                
            
            
    

        
            