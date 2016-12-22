class Solution(object):
    """
    Find optimal solution; greedy or dp; try greedy first
    
    Explanation

    Let reach be the maximum reach. Meaning we already know we can build all sums in [0,reach]. Then if we have a number num <= (reach+1) in the given array, we can add it to build all sums in [0, reach+num]. @Why? Because we already build all sums in [0,reach] then we can build all sums in [reach+1, reach+num] by adding num to sums in [0,reach]. And intuitively, the maximum reach we can get is (reach+num).@ If we don't, then we must add such a number to the array, and it's best to add (reach+1) itself, to maximize the reach.

    Example: Let's say the input is nums = [1, 2, 4, 13, 43] and n = 100. We need to ensure that all sums in the range [1,100] are possible.

    Using the given numbers 1, 2 and 4, we can already build all sums from 0 to 7, i.e., the range [0,7]. But we can't build the sum 8, and the next given number (13) is too large. So we insert 8 into the array. Then we can build all sums in [0,15].

    Do we need to insert 16 into the array? No! We can already build the sum 3, and adding the given 13 gives us sum 16. We can also add the 13 to the other sums, extending our range to [0,28].

    And so on. The given 43 is too large to help with sum 29, so we must insert 29 into our array. This extends our range to [0,57]. But then the 43 becomes useful and expands our range to [0,100]. At which point we're done.
    """
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        cnt = 0; reach = 0; i = 0
        while reach < n:
            if i < len(nums) and reach + 1 >= nums[i]:
                reach += nums[i]
                i += 1
            else:
                cnt += 1
                reach += (reach + 1)
        return cnt
            
            
        
