# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    def getInDegree(self, graph):
        in_degree = dict()
        if node in graph:  # miss
           in_degree[node] = 0  # miss
        for node in graph: 
            for neighbor in node.neighbors:
                in_degree[neighbor] += 1
        return in_degree
        
    def getLeaves(self, in_degree):
        leaves = [node for node in in_degree if in_degree[node] == 0]
        return leaves
            
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """
    def topSort(self, graph):
        # write your code here
        in_degree = self.getInDegree(graph)
        leaves = self.getLeaves(in_degree)
        result = list()
        while leaves:
            result += leaves[:]
            size = len(leaves)
            for _ in range(size):
                leaf = leaves.pop(0)
                for neighbor in leaf.neighbors:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        leaves.append(neighbor)
        return result
            
