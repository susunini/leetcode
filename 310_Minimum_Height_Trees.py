class Solution(object):
    """ Topological Sort on a Undirected Graph. 48%. """
    def getNeighbors(self, n, edges):
        neighbors = collections.defaultdict(set)
        for node1, node2 in edges:
            neighbors[node1].add(node2)
            neighbors[node2].add(node1)
        return neighbors
    
    def getLeaves(self, neighbors):
        return [node for node in neighbors if len(neighbors[node]) == 1]
            
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        neighbors = self.getNeighbors(n, edges)
        leaves = self.getLeaves(neighbors)
        not_removed = set([node for node in range(n)])
        while len(not_removed) > 2:
            size = len(leaves)
            for _ in range(size):
                node = leaves.pop(0)
                not_removed.remove(node)
                for neighbor in neighbors[node]:
                    neighbors[neighbor].remove(node)
                    if len(neighbors[neighbor]) == 1:
                        leaves.append(neighbor)
        return list(not_removed)
        
