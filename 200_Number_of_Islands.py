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
        if len(grid) < 1 or len(grid[0]) < 1:
            return 0
        self.count = 0 # Wrong: count = 0
        m = len(grid)
        n = len(grid[0])
        parents = [None]*(m*n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.count += 1
        
        for i in range(len(parents)):
            parents[i] = i
        
        def getRoot(e):
            while e != parents[e]:
                e = parents[e]
            return e
        
        def isConnected(e1, e2):
            return getRoot(e1) == getRoot(e2)
            
        def union(e1, e2):
            """ union two elements. 
            :return False if e1 and e2 is already connected; 
            otherwise return True. """
            r1, r2 = getRoot(e1), getRoot(e2)
            if r1 == r2:
                return False
            parents[r1] = r2
            self.count -= 1 # important
            return True
            
        def getIndex(x, y):
            return x*n + y
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    for x,y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            union(getIndex(i,j), getIndex(x,y))
                        
        return self.count
        
        
