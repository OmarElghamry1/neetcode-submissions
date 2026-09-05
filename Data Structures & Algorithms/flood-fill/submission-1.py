class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        if image[sr][sc] == color: 
            return image

        orig = image[sr][sc]
        n, m = len(image), len(image[0])

        def dfs(sr, sc): 

            if not (0 <= sr < n and 0 <= sc < m) or image [sr][sc] != orig: 
                return 


            image[sr][sc] = color

            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)
            
        
        dfs(sr, sc)
        return image
            
        
        


            







    
        