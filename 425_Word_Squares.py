""" Google. Hard. Trie. Backtracing. 41%. """
class TrieNode(object):
    def __init__(self):
        self.children = dict()
        self.startWith = list()
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def buildTrie(self, words):
        for i, w in enumerate(words):
            cur = self.root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
                cur.startWith.append(i)
    
    def getStartWith(self, prefix):
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        return cur.startWith
            
    
class Solution(object):
    def helper(self, words, trie, square, res):
        if len(square) == len(words[0]):
            res.append(square[:])
            return
        for index in trie.getStartWith(''.join(zip(*square)[len(square)])):
            self.helper(words, trie, square+[words[index]], res) #
        
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = Trie(); trie.buildTrie(words)
        res = []
        for w in words:
            square = [w]
            self.helper(words, trie, square, res)
        return res
