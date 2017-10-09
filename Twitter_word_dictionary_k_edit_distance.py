"""
Given a dictionary and a word w, find all words from the dictionary whose edit distance from w is k.
http://stevehanov.ca/blog/index.php?id=114
"""

class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for i, letter in enumerate(word):
            if letter not in node.children: 
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.word = word

def buildTrie(wordDict):
    trie = Trie()
    for word in wordDict:
        trie.insert(word)
    return trie

def search(trie, word, max_dist):
    results = list()
    cur_row = range(len(word)+1) # row for dp matrix
    for letter, child in trie.root.children.items():
        doSearch(child, letter, word, max_dist, cur_row, results)
    return results


def doSearch(node, letter, word, max_dist, prev_row, results):
    cur_row = [None]*(len(word)+1)
    cur_row[0] = prev_row[0]+1
    for j in range(1, len(cur_dp_row)):
        insert_cost = prev_dp_row[j]+1
        delete_cost = cur_dp_row[j-1]+1
        replace_cost = prev_dp_row[j-1] + (0 if letter == word[j-1] else 1)
        cur_row[j] = min(insert_cost, delete_cost, replace_cost)
    if cur_dp_row[-1] <= max_dist and node.word is not None:
        results.append(node.word)
        
    if min(cur_dp_row) > max_dist:
        return

    for letter, child in node.children.items():
        doSearch(child, letter, word, max_dist, cur_row, results)

dictionary = ['bat', 'batt', 'cat', 'beetle']
trie = buildTrie(dictionary)
assert(search(trie, 'bat', 1) == ['cat', 'bat', 'batt'])
assert(search(trie, 'beatle', 1) == ['beetle'])





