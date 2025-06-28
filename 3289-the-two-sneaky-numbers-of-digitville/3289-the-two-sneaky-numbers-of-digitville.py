class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        ans = []
        for i in range(len(nums)):
            if nums[i] in seen:
                ans.append(nums[i])
            else:
                seen.add(nums[i])

        return ans

        