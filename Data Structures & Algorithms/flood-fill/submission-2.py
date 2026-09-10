class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
   
        orig = image[sr][sc]
        if orig == color: 
            return image

        image[sr][sc] = color
    
        n, m = len(image), len(image[0])

        q = collections.deque()
        q.append([sr, sc])


        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q: 
            for _ in range(len(q)): 
                sr, sc = q.popleft()
                for dr, dc in directions: 
                    
                    r, c = sr + dr, sc + dc
                    if (r in range(n) and c in range(m) and 
                    image[r][c] == orig): 
                            image[r][c] = color
                            q.append([r, c])

                    
        return image
