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
                
