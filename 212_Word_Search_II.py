class TrieNode(object):
    def __init__(self):
        self.children = dict()
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                new_node = TrieNode()
                cur.children[ch] = new_node
            cur = cur.children[ch]
        cur.children['#'] = True
        
    def buildTrie(self, words):
        for w in words:
            self.addWord(w)
            
class Solution(object):
    """ Wrong. """
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        trie.buildTrie(words)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.root, '', res)
        return res
    
    def dfs(self, board, i, j, root, word, res):
        if '#' in root.children:
            res.append(word)
        n = len(board); m = len(board[0])
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        ch = board[i][j]
        if ch not in root.children:
            return
        next_root = root.children[ch]
        next_word = word + ch
        self.dfs(board, i+1, j, next_root, next_word, res)
        self.dfs(board, i-1, j, next_root, next_word, res)
        self.dfs(board, i, j+1, next_root, next_word, res)
        self.dfs(board, i, j-1, next_root, next_word, res)
        
class Solution(object):
    """ Trie. Backtracing. """
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        trie.buildTrie(words)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, trie.root, '', res)
        return res
    
    def dfs(self, board, i, j, root, word, res):
        if '#' in root.children:
            res.append(word)
            del root.children['#'] # de-duplicate
        n = len(board); m = len(board[0])
        if i < 0 or i >= n or j < 0 or j >= m:
            return
        ch = board[i][j]
        if ch not in root.children:
            return
        next_root = root.children[ch]
        next_word = word + ch
        tmp = board[i][j]; board[i][j] = None # cannot be reused
        self.dfs(board, i+1, j, next_root, next_word, res)
        self.dfs(board, i-1, j, next_root, next_word, res)
        self.dfs(board, i, j+1, next_root, next_word, res)
        self.dfs(board, i, j-1, next_root, next_word, res)
        board[i][j] = tmp
                
        
        
