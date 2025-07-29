class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for _ in range(k):
            min_num = min(nums)
            index = nums.index(min_num)
            nums[index] = -min_num

        return sum(nums)
        