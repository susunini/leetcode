""" Union Find. Wrong. """
class IslandUnionFind(object):
    def __init__(self, grid):
        self.grid = grid
        self.count = 0
        self.dic = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.dic[(i,j)] = (i,j)
                    self.count += 1

    def findRoot(self, e):
        while e != self.dic[e]:
            e = self.dic[e]
        return e
        
    def union(self, e1, e2):
        i, j = e2
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]):
            return 
        if self.grid[i][j] != 1:
            return
        r1 = self.findRoot(e1)
        r2 = self.findRoot(e2)
        if r1 == r2:
            return
        self.dic[e2] = e2
        self.count -= 1
        
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        iuf = IslandUnionFind(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    iuf.union((i,j), (i-1,j))
                    iuf.union((i,j), (i+1,j))
                    iuf.union((i,j), (i,j-1))
                    iuf.union((i,j), (i, j+1))
        return iuf.count
        
" Union Find. 332ms(3.5%). """
class IslandUnionFind(object):
    def __init__(self, grid):
        self.grid = grid
        self.count = 0
        self.dic = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dic[(i,j)] = (i,j)
                    self.count += 1

    def findRoot(self, e):
        while e != self.dic[e]:
            e = self.dic[e]
        return e
        
    def union(self, e1, e2):
        i, j = e2
        if i < 0 or i >= len(self.grid) or j < 0 or j >= len(self.grid[0]):
            return 
        if self.grid[i][j] != '1':
            return
        r1 = self.findRoot(e1)
        r2 = self.findRoot(e2)
        if r1 == r2:
            return
        self.dic[r2] = r1
        self.count -= 1
        

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        iuf = IslandUnionFind(grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    iuf.union((i,j), (i-1,j))
                    iuf.union((i,j), (i+1,j))
                    iuf.union((i,j), (i,j-1))
                    iuf.union((i,j), (i, j+1))
        return iuf.count
    
""" Union Find. Use 1-D array instead of dict. 282ms(5%). """
class IslandUnionFind(object):
    def __init__(self, grid):
        self.grid = grid
        self.count = 0
        m = len(grid); n = len(grid[0])
        self.roots = [0]*(m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.count += 1
        for i in range(m*n):
            self.roots[i] = i

    def findRoot(self, p):
        while p != self.roots[p]:
            p = self.roots[p]
        return p
        
    def union(self, e1, e2):
        m = len(self.grid); n = len(self.grid[0])
        i1, j1 = e1; i2, j2 = e2
        if i2 < 0 or i2 >= m or j2 < 0 or j2 >= n:
            return 
        if self.grid[i2][j2] != '1':
            return
        p1 = i1*n+j1; p2 = i2*n+j2
        r1 = self.findRoot(p1)
        r2 = self.findRoot(p2)
        if r1 == r2:
            return
        self.roots[r2] = r1
        self.count -= 1
        

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0
        iuf = IslandUnionFind(grid)
        m = len(grid); n = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != '1':
                    continue
                iuf.union((i,j), (i-1,j))
                iuf.union((i,j), (i+1,j))
                iuf.union((i,j), (i,j-1))
                iuf.union((i,j), (i, j+1))
        return iuf.count
        
        
