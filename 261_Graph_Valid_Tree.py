class Solution(object):
    """ Topological Sort on an Undirected Graph. 14%. 
    Any valid tree has (n-1) edges given n nodes and there is no cycle in the tree. 
    If satisfying these two conditions, guarantee to be connected. 
    Test Cases 1. 0 2. 0-1 3. 0 1-2-3 4. 0 1-2-3 1-3 5. 0-1-2-3 1-3 """
    def getNeighbors(self, n, edges):
        neighbors = collections.defaultdict(set)
        for node1, node2 in edges:
            neighbors[node1].add(node2)
            neighbors[node2].add(node1)
        return neighbors
    
    def getLeaves(self, neighbors):
        return [node for node in neighbors if len(neighbors[node]) == 1]
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False
        neighbors = self.getNeighbors(n, edges)
        leaves = self.getLeaves(neighbors); n -= len(leaves)
        while leaves:
            size = len(leaves)
            for _ in range(size):
                node = leaves.pop(0)
                for neighbor in neighbors[node]:
                    neighbors[neighbor].remove(node)
                    if len(neighbors[neighbor]) == 1:
                        leaves.append(neighbor); n -= 1
        return n == 1 or n == 0
