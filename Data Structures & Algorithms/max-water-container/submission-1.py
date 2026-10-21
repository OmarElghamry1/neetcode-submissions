class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L, R = 0, len(heights) - 1
        area = 0

        while L < R: 
            cur_area = (R - L ) * min(heights[L], heights[R])
            area = max(area, cur_area)

            if heights[L] < heights[R]: 
                L += 1
            else: 
                R -= 1
        
        return area





        