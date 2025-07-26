class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            for j in range(len(nums)-1,-1,-1):
                left = i + 1
                right = j - 1

                if j < len(nums)-1 and nums[j] == nums[j+1]:
                    continue

                while left < right:
                    if nums[i]+nums[j]+nums[left]+nums[right] == target:
                        result.append([nums[i],nums[j],nums[left],nums[right]])
                        left +=1

                        while left - 1 != 0 and left < right and nums[left] == nums[left-1]:
                            left += 1
                        while right + 1 != len(nums)-1 and left < right and nums[right] == nums[right+1]:
                            right += 1
                    
                    elif nums[i]+nums[j]+nums[left]+nums[right] > target:
                        right -= 1

                    else:
                        left +=1

        return result



        