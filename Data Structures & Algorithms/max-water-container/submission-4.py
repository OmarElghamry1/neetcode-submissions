class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L, R = 0, len(heights) - 1
        area = 0

        while L < R: 
            h = min(heights[L], heights[R]) # height
            w = R - L # width
            area = max(area, h * w)

            if heights[L] < heights[R]: 
                L += 1
            
            else: 
                R -= 1
        
        return area




        
    

      

  
            
        
            

        