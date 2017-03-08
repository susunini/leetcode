class Solution(object):
    """ Wrong. """
    def share(self, w1, w2):
        b1 = 0
        for ch in w1:
            b1 = b1|(1<<(ch-'a'))
        b2 = 0
        for ch in w2:
            b2 = b2|(1<<(ch-'a'))
        return b1 & b2
            
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                w1 = words[i]; w2 = words[j]
                if not self.share(w1, w2):
                    res = max(res, len(w1)*len(w2))
        return res
        
class Solution(object):
    """ TLE. """
    def share(self, w1, w2):
        b1 = 0
        for ch in w1:
            b1 = b1|(1<<(ord(ch)-ord('a')))
        b2 = 0
        for ch in w2:
            b2 = b2|(1<<(ord(ch)-ord('a')))
        return b1 & b2
            
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                w1 = words[i]; w2 = words[j]
                if not self.share(w1, w2):
                    res = max(res, len(w1)*len(w2))
        return res
        
 class Solution(object):
    """ Bit Manipulation. Beats 60%. 
    
    1. Prune the search space by sorting words by length first.
    2. Pre-calcuate masks
    """
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len, reverse=True)
        masks = [0] * len(words)
        for i in range(len(words)):
            for ch in words[i]:
                masks[i] |= (1<<(ord(ch)-ord('a')))
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                w1 = words[i]; w2 = words[j]
                if not (masks[i] & masks[j]):
                    res = max(res, len(w1)*len(w2))
                    break
        return res
        
  class Solution(object):
    """ Further pruning. But time does not improve. """
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len, reverse=True)
        masks = [0] * len(words)
        for i in range(len(words)):
            for ch in words[i]:
                masks[i] |= (1<<(ord(ch)-ord('a')))
        res = 0
        for i in range(len(words)):
            if i != len(words)-1 and len(words[i])*len(words[i+1]) <= res: 
                break
            for j in range(i+1, len(words)):
                w1 = words[i]; w2 = words[j]
                if not (masks[i] & masks[j]):
                    res = max(res, len(w1)*len(w2))
                    break
        return res
                
        
