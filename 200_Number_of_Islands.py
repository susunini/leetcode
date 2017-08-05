class Solution(object):
    """ Backtracing. 156ms(40%). """
    def dfs(self, i, j, grid):
        m = len(grid); n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] != '1':
            return
        grid[i][j] = 'X'
        self.dfs(i-1, j, grid)
        self.dfs(i+1, j, grid)
        self.dfs(i, j-1, grid)
        self.dfs(i, j+1, grid)
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(i, j, grid)
        return res
    
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = 'X'
                map(dfs, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(
            dfs(i,j) for i in range(len(grid)) for j in range(len(grid[i]))
            )
    
class Solution(object):
    """ Union Find. 2nd Round. 188ms(23%). 
    
    Summary of union find
    1. maintain two variables
    count - count of unions
    parents - parent of each element
    initialize count and parents first
    2. methods
    getRoot(e) - root's parent is itself
    isConnected(e1, e2) - find roots of e1 and e2 return True if roots are equal otherwise return False
    union(e1, e2) - find roots of e1 and e2 return True if roots are equal; otherwise set root of e1 
    as root e2 or vice versa and return True.
    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        
        self.count = sum([1 for i in range(m) for j in range(n) if grid[i][j] == '1']) # Wrong: count =
        parents = [i for i in range(m*n)]
        
        def getIndex(row, col):
            return row*n+col # Wrong: row*m+col
        
        def getRoot(node):
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return node
        
        def union(node1, node2):
            root1 = getRoot(node1)
            root2 = getRoot(node2)
            if root1 == root2:
                return
            parents[root1] = root2
            self.count -= 1
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                for x, y in [(i-1, j), (i, j-1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        union(getIndex(i,j), getIndex(x,y))
                        
        return self.count
        
        
