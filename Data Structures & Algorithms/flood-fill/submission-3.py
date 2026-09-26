class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orig = image[sr][sc]

        if orig == color: 
            return image
        
        n, m = len(image), len(image[0])

        q = collections.deque()
        visit = set()

        image[sr][sc] = color
        q.append([sr, sc])
        visit.add((sr, sc))

        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q: 
            for _ in range(len(q)): 

                row, col = q.popleft()

                for dr, dc in directions: 

                    r, c = row + dr, col + dc

                    if (r in range(n) and c in range(m) \
                        and (r, c) not in visit and image[r][c] == orig): 
                            visit.add((r, c))
                            image[r][c] = color
                            q.append([r, c])
            
        return image





   
      