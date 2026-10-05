class Solution:
    def climbStairs(self, n: int) -> int:
        
        first, second = 1, 1

        for i in range(n): 
            tmp = second
            second = first + second
            first = tmp
        
        return first

        

            


            
                
            
            
    

        
            