""" Trie. 495ms(39%). 

Faster if using dict/defaultdict.
"""

class TrieNode(object):
    def __init__(self):
        self.children = [None]*27
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def getIndex(self, ch):
        return ord(ch) - ord('a')
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for ch in word:
            index = self.getIndex(ch)
            if not cur.children[index]:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.children[-1] = '#'
            
            
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for ch in word:
            index = self.getIndex(ch)
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return cur.children[-1] == '#'
            
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for ch in prefix:
            index = self.getIndex(ch)
            if not cur.children[index]:
                return False
            cur = cur.children[index]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
