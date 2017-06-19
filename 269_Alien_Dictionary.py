class Solution(object):
    """ Wrong. Incorrect understanding of the problem description. """
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        chars = set(''.join(words))
        indeg, outdeg = dict(), dict()
        for char in chars:
            indeg[char] = set()
            outdeg[char] = set()
            
        words.insert(0, ''.join([word[0] for word in words if word]))
        
        for word in words:
            for i in range(1, len(word)):
                start, end = word[i-1], word[i]
                if start != end:
                    outdeg[start].add(end)
                    indeg[end].add(start)
                    
        res = []
        leaves = [char for char, char_set in indeg.items() if not char_set]
        while leaves:
            res += leaves
            for start in leaves:
                del indeg[start]
                for end in outdeg[start]:
                    indeg[end].remove(start)
            leaves = [char for char, char_set in indeg.items() if not char_set]
        return ''.join(res) if not indeg else ''
    
class Solution(object):
    """ Graph. Topological Sort. 49ms(49%). """
    def getFirstDiff(self, word1, word2):
        n = min(len(word1), len(word2))
        for i in range(n):
            if word1[i] != word2[i]:
                return i
        return None
        
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        unique = set(''.join(words))
        n = len(unique)
        
        indeg = collections.defaultdict(int)
        outdeg = collections.defaultdict(list)
        for i in range(1, len(words)):
            j = self.getFirstDiff(words[i-1], words[i])
            if j != None:  # Wrong- if j: 
                start, end = words[i-1][j], words[i][j]
                indeg[end] += 1
                outdeg[start].append(end)
                
        res = []
        leaves = [ch for ch in unique if indeg[ch] == 0]
        while leaves:
            res += leaves
            n -= len(leaves)
            new_leaves = []
            for start in leaves:
                for end in outdeg[start]:
                    indeg[end] -= 1
                    if indeg[end] == 0:
                        new_leaves.append(end)
            leaves = new_leaves
                        
        return ''.join(res) if n == 0 else ''
            
        
class Solution(object):
    """  StefanPochmann's Solution 1. 10%. """
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        less = [] # edges less[0] list of start less[1] list of end
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    less += a + b,
                    break
        chars = set(''.join(words))
        order = []
        while less:
            free = chars - set(zip(*less)[1]) # free- leaves
            if not free:
                return ''
            order += free
            less = filter(free.isdisjoint, less) 
            chars -= free
        return ''.join(order + list(chars))

class Solution(object):
    """ StefanPochmann's Solution 2. """
    def alienOrder(self, words):
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b)
                    pre[b].add(a)
                    break
        chars = set(''.join(words))
        free = chars - set(pre)
        order = ''
        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]:
                    free.add(b)
        return order * (set(order) == chars)
                
        
