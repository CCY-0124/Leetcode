class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if sum(nums)- k < 0:
            return sum(nums)
        if sum(nums)//k == 0:
            return 0
        else:
            return sum(nums)%k
        