class Solution:
    def maxArea(self, heights: List[int]) -> int:

        L = 0
        R = len(heights) - 1
        max_area = 0
        
        
        while L < R: 
            h = min(heights[L], heights[R])
            max_area = max(max_area, h * (R - L))

            if heights[L] < heights[R]: 
                L += 1
            elif heights[L] > heights[R]: 
                R -= 1
            else: 
                R -= 1

        return max_area
            
            
        
            

        