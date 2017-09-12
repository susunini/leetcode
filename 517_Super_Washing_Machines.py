class Solution(object):
    """" Hard. DP. """
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        if not machines:
            return 0
        # get average
        avg, mod = divmod(sum(machines), len(machines))
        if mod:
            return -1
        # get gain/lose array
        gain_lose = [num-avg for num in machines]
        # find peak
        count = gain_lose[0]
        result = abs(gain_lose[0])
        for i in range(1, len(gain_lose)):
            count += gain_lose[i]
            result = max(result, abs(count), gain_lose[i]) # Wrong: result = max(result, abs(count))
        return result
