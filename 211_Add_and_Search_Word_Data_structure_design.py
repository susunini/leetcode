class TrieNode(object):
    def __init__(self):
        self.children = dict()
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.children['#'] = True
        
    def helper(self, root, word):
        if not word:
            return '#' in root.children
        cur = root
        for i, ch in enumerate(word):
            if ch != '.':
                if ch not in cur.children:
                    return False
                cur = cur.children[ch]
            else:
                for ch, child in cur.children.items():
                    if ch != '#' and self.helper(child, word[i+1:]): # Wrong: if self.helper(child, word[i+1:]):
                        return True
                return False
        return '#' in cur.children
                
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(self.root, word)

                
                
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
