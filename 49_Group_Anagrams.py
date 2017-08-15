class Solution(object):
    def getHashKey(self, cur_str):
        return ''.join(sorted(cur_str))
            
        
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        match = collections.defaultdict(list)
        for cur_str in strs:
            match[self.getHashKey(cur_str)].append(cur_str)
        return [li for _, li in match.items()]
            
        
