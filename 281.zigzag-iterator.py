#
# [281] Zigzag Iterator
#
# https://leetcode.com/problems/zigzag-iterator
#
# Medium (50.16%)
# Total Accepted:
# Total Submissions:
# Testcase Example:  '[1,2]\n[3,4,5,6]'
#
#
# Given two 1d vectors, implement an iterator to return their elements
# alternately.
#
#
# For example, given two 1d vectors:
#
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
#
#
#
# By calling next repeatedly until hasNext returns false, the order of elements
# returned by next should be: [1, 3, 2, 4, 5, 6].
#
#
#
# Follow up: What if you are given k 1d vectors? How well can your code be
# extended to such cases?
#
#
# Clarification for the follow up question - Update (2015-09-18):
# The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases.
# If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For
# example, given the following input:
#
# [1,2,3]
# [4,5,6,7]
# [8,9]
#
# It should return [1,4,8,2,5,9,3,6,7].
#
#
class ZigzagIterator(object):
   """ Google. Design. """

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.lists = [v1, v2]
        self.pointers = [0 if li else sys.maxint for li in self.lists]



    def next(self):
        """
        :rtype: int
        """
        pointer = min(self.pointers)
        list_index = self.pointers.index(pointer)
        list = self.lists[list_index]
        res = list[pointer]
        self.pointers[list_index] += 1
        if self.pointers[list_index] >= len(list):
            self.pointers[list_index] = sys.maxint
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return any([self.pointers[i] != sys.maxint for i in range(len(self.pointers))])


# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
