class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols=len(grid),len(grid[0])
        visited=set()
        islands=0

        def bfs(rows,cols):
            q=collections.deque()
            visited.add((rows,cols))
            q.append((rows,cols))

            while q:
                rows,cols=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    r,c=rows+dr,cols+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c]=="1" and (r,c) not in visited):
                        q.append(r,c)
                        visit.append(r,c)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r,c)
                    islands+=1
        return islands
