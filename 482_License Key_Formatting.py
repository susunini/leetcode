class Solution(object):
    """ Google. String. """
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = S.replace('-', '')[::-1]
        res = '-'.join([res[i:i+K] for i in range(0, len(res), K)])[::-1]
        return res
