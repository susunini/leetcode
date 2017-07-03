class Solution(object):
    """ Two-End BFS. 128ms(97%). 
    Test Cases: 1. beginWord = "hit" endWord = "cog" wordList = ["hot","dot","dog","lot","log","cog"] => return 5
    2. beginWord = "hit" endWord = "cog" wordList = ["hot","dot","dog","lot","log"] return 0
    2. beginWord = "hit" endWord = "hit" wordList = ["hot","dot","dog","lot","log"] return 1
    3. beginWord = "hit" endWord = "hot" wordList = ["hot","dot","dog","lot","log"] return 2
    """
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0
        wordDict = set(wordList); wordDict.discard(beginWord)  # Wrong: wordDict.remove(beginWord)
        front = set([beginWord]); back = set([endWord]) # Wrong: front = set(beginWord); back = set(endWord)
        length = 2
        while front:
            front = wordDict & set(word[:i]+ch+word[i+1:]
                for word in front
                for i in range(len(word))
                for ch in 'abcdefghijklmnopqrstuvwxyz'
            )
            if front & back:
                return length
            length += 1
            if len(front) > len(back):  # Wrong: if len(front) < len(back):
                front, back = back, front
            wordDict -= front
        return 0