class Solution(object):
    """ Tree. Tree Traversal. """
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for i, id_ in enumerate(ppid):
            d[id_].append(pid[i])
        stack = [kill]
        res = []
        while stack:
            id_ = stack.pop()
            res.append(id_)
            stack.extned(d[id_])
        return res
        
class Solution(object):
    """ Faster using extend of list. """
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = collections.defaultdict(list)
        for i, id_ in enumerate(ppid):
            d[id_].append(pid[i])
        stack = [kill]
        res = []
        while stack:
            id_ = stack.pop()
            res.append(id_)
            stack.extend(d[id_])
        return res
            
            
