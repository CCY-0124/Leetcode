class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        for i in range(k):
            pos = nums.index(min(nums))
            nums[pos] = nums[pos] * multiplier

        return nums
            
        