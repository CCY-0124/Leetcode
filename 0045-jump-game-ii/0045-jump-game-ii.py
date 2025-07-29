class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        counter = 0
        max_reach = 0
        end = 0

        for i in range(len(nums)):
            max_reach = max(max_reach, i+nums[i])
            print(max_reach)
            if max_reach >= len(nums)-1:
                counter +=1
                return counter
            if i == end:
                counter +=1
                end = max_reach

        return counter
