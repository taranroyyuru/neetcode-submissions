from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = collections.deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        start = 0 # start 5
        count = 0
        minutes = 0 
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    start += 1
                if grid[r][c] == 2:
                    q.append((r,c))  #added (2,2)

        while q and start > count:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr 
                    col = c + dc
                    if (row >= 0 and row < ROWS
                        and col >= 0 and col < COLS
                        and grid[row][col] == 1):
                        count += 1
                        grid[row][col] = 2
                        q.append((row,col)) #added ((2,1),(1,2))
            minutes += 1

        if count == start:
            return minutes 
        else:
            return -1

        



        


        