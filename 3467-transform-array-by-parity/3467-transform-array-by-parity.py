class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new = [0 if num%2 == 0 else 1 for num in nums].sort()
        return new
        