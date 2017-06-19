# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """ Wrong. """
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: 
            return None
        match = dict()
        queue = [node]
        while queue:
            node = queue.pop(0)
            if node not in match:
                new_node = UndirectedGraphNode(node.label)
                match[node] = new_node
                queue += node.neighbors
        for node, new_node in match.items():
            new_node.neighbors = [match[neighbor] for neighbor in node.neighbors]
        return match[node]

class Solution:
    """ Graph. 30%. """
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: 
            return None
        match = dict()
        queue = [node]
        while queue:
            cur_node = queue.pop(0)
            if cur_node not in match:
                new_node = UndirectedGraphNode(cur_node.label)
                match[cur_node] = new_node
                queue += cur_node.neighbors
        for cur_node, new_node in match.items():
            new_node.neighbors = [match[neighbor] for neighbor in cur_node.neighbors]
        return match[node]
        
        
                
