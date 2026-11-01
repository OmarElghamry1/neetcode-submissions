class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_h = 0

        while L < R: 
            h = min(heights[L], heights[R])
            max_h = max(max_h, h * (R - L))
            if heights[L] < heights[R] :
                L += 1
            
            elif heights[L] > heights[R]: 
                R -= 1
            
            else: 
                R -= 1


        return max_h

  
            
        
            

        