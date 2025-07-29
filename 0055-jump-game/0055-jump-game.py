class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = [i+x for i,x in enumerate(nums)]

        print(max_reach)

        if len(nums) == 1:
            return True

        farest = 0
        for i in range(len(nums)):
            farest = max(max_reach[i], farest)
            if i >= farest:
                return False
            
            elif (i + nums[i]) >= len(nums)-1:
                return True
        