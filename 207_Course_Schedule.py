class Solution(object):
    """ Topological Sort (BFS). 55ms(94%).
    """
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0] * numCourses
        outdegree = [[] for _ in range(numCourses)]
        
        for end, start in prerequisites:
            indegree[end] += 1
            outdegree[start].append(end)
        
        n = numCourses
        leaves = [i for i in range(len(indegree)) if indegree[i] == 0]
        while leaves:
            n -= len(leaves)
            if n == 0:
                break
            new_leaves = []
            for node in leaves:
                for end_node in outdegree[node]:
                    indegree[end_node] -= 1
                    if indegree[end_node] == 0:
                        new_leaves.append(end_node)
                leaves = new_leaves
        return n == 0
            
        
