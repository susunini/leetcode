
class Solution(object):
    """
    Solution 1:
    explanation:
    https://leetcode.com/discuss/60408/sharing-explanation-of-the-solution
    another good explanation:
    https://discuss.leetcode.com/topic/21605/accepted-c-java-o-n-time-o-1-space-easy-solution-with-detail-explanations
    Name the two numbers as A and B
    step 1: Find aXorb, the xor(exclusive or) value of A and B
    step 2: From aXorb, we can find lastBit, the lowest bit which can differentiate A from B
    step 3: lastBit help divide nums into two groups, one with the bit set and the other unset. XOR numbers in each group.
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        aXorb = 0
        for num in nums:
            aXorb ^= num
        lastBit = 1
        while not (lastBit & aXorb): 
            lastBit <<= 1
        A = B = 0
        for num in nums:
            if lastBit & num:
                A ^= num
            else:
                B ^= num
        return [A, B]
        
class Solution(object):
    """
    Solution 2:
    Difference from Solution 1, to get the different bit at the lowest position
    lastBit = aXorb & (-aXorb)
    """
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        aXorb = 0
        for num in nums:
            aXorb ^= num
        lastBit = aXorb & (-aXorb)
        A = B = 0
        for num in nums:
            if lastBit & num:
                A ^= num
            else:
                B ^= num
        return [A, B]
