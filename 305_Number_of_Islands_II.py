class Solution(object):
    """ Union Find. 522ms(53%). """
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        res = []
        self.count = 0
        parents = [None]*(m*n)
        for i in range(m*n):
            parents[i] = i
        grid = [[0]*n for _ in range(m)]
        
        def getRoot(e):
            while e != parents[e]:
                e = parents[e]
            return e
            
        def union(e1, e2):
            r1 = getRoot(e1)
            r2 = getRoot(e2)
            if r1 == r2:
                return False
            parents[r1] = r2
            self.count -= 1
            return True
            
        def getIndex(x, y):
            return x*n+y
        
        for x, y in positions:
            if grid[x][y] != 1:
                grid[x][y] = 1; self.count += 1
                for x1, y1 in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= x1 < m and 0 <= y1 < n and grid[x1][y1] == 1:
                        union(getIndex(x, y), getIndex(x1, y1))
            res.append(self.count)
        return res
        
