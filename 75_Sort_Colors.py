class Solution(object):
    """ Sort.
    At any time, A[0:i] all 0, A[i:j] all 1, A[k+1:] all 2 """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = j = 0; k = len(nums) - 1
        while j <= k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1; j += 1
            elif nums[j] == 1:
                j += 1
            else: # nums[j] == 2
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
                
                
class Solution(object):
    """ 20170629. Sort. Two Pointers.
    Maintain: nums before p1 are all 1s, nums after p2 are all 2s, all nums [p1, c] all 1s unless p1 == c
    test cases: [0], [0,0]. """
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p1 = 0; p2 = len(nums)-1
        c = 0
        while c <= p2 and p1 < p2:
            if nums[c] == 1:
                c += 1
            elif nums[c] == 2:
                nums[c], nums[p2] = nums[p2], nums[c]
                p2 -= 1
            else: # nums[c] == 0
                nums[c], nums[p1] = nums[p1], nums[c]
                p1 += 1
