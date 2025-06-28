class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        first_half = nums[:n]
        #second_half = nums
        for i in range(1,len(nums),2):
            first_half.insert(i,nums[n])
            n += 1
        return first_half