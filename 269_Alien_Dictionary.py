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
            
                
        
