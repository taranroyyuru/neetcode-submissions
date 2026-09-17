from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        q = collections.deque()
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    res += 1
                    grid[r][c] = "0"
                    q.append([r,c])
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            row = r + dr
                            col = c + dc
                            if(row >= 0 and row < ROWS and
                                col >= 0 and col < COLS and
                                grid[row][col] == "1"):
                                grid[row][col] = "0"
                                q.append([row, col])
        return res




        