from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0
        q = collections.deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    q.append([r,c])
                    res += 1
                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            row = dr + r
                            col = dc + c
                            if ( 0 <= row and row < ROWS
                                and 0 <= col and col < COLS
                                and grid[row][col] == "1"):
                                grid[row][col] = "0"
                                q.append([row, col])
        return res
                    



        