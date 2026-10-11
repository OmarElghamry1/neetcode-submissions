class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]

        if orig == color: 
            return image
        
        image[sr][sc] = color
        
        m, n = len(image), len(image[0])

        q = collections.deque()
        q.append([sr, sc])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        while q: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    if (r in range(m) and c in range(n) and 
                        image[r][c] == orig): 
                            image[r][c] = color
                            q.append([r, c])
        
        return image




        





   
      