class Solution(object):
    """ Graph. DFS. 65ms(87%). """
    def dfs(self, node, graph, visited):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, graph, visited)
    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        res = 0
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                res += 1
                self.dfs(i, graph, visited)
                
        return res
        
class Solution(object):
    """ Graph. BFS. Slow. """
    def bfs(self, root, graph, visited):
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [False]*n
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                self.bfs(i, graph, visited)
                print visited
        return res
        
class Solution(object):
    """ Graph. BFS. 100%. """
    def bfs(self, root, graph, visited):
        queue = [root]
        for node in queue:
            if not visited[node]:
                queue += graph[node]
                visited[node] = True
                
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [False]*n
        graph = [[] for _ in range(n)]
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                self.bfs(i, graph, visited)
        return res

""" Graph. Union Find. Slow. """
class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.parents = [0]*n
        for i in range(n):
            self.parents[i] = i
    
    def findRoot(self, e):
        while e != self.parents[e]:
            e = self.parents[e]
        return e
    
    def union(self, e1, e2):
        r1 = self.findRoot(e1)
        r2 = self.findRoot(e2)
        if r1 == r2:
            return
        self.parents[r2] = r1
        self.count -= 1
    
class Solution(object):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)
        for i, j in edges:
            uf.union(i, j)
        return uf.count

""" Graph. Union Find. Faster using path compression. (54%). """
class UnionFind(object):
    def __init__(self, n):
        self.count = n
        self.parents = [0]*n
        for i in range(n):
            self.parents[i] = i
    
    def findRoot(self, e):
        while e != self.parents[e]:
            self.parents[e] = self.parents[self.parents[e]] # path compression
            e = self.parents[e]
        return e
    
    def union(self, e1, e2):
        r1 = self.findRoot(e1)
        r2 = self.findRoot(e2)
        if r1 == r2:
            return
        self.parents[r2] = r1
        self.count -= 1
    
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uf = UnionFind(n)
        for i, j in edges:
            uf.union(i, j)
        return uf.count
    
class Solution(object):
    """ Graph. Union Find. Nested functions. 68ms(91%). """
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.count = n
        parents = [i for i in range(n)]
    
        def findRoot(e):
            while e != parents[e]:
                parents[e] = parents[parents[e]] # path compression
                e = parents[e]
            return e
    
        def union(e1, e2):
            r1 = findRoot(e1)
            r2 = findRoot(e2)
            if r1 == r2:
                return
            parents[r2] = r1
            self.count -= 1
        
        for i, j in edges:
            union(i, j)
        return self.count
        
        
        
        
        
        
        
