class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc]== color: 
            return image

        nrow, ncol = len(image), len(image[0])
        value = image[sr][sc]
        q = collections.deque()
        q.append((sr, sc))

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q: 
            for _ in range(len(q)): 
                row, col = q.popleft()
                image[row][col] = color
                for dr, dc in directions: 
                    r, c = row+dr, col + dc
                    if (min(r, c) < 0 or r >= nrow 
                        or c >= ncol or image[r][c] == color): 
                            continue
                    if image[r][c] == value: 
                        q.append((r, c))
            
                
        return image


            







    
        