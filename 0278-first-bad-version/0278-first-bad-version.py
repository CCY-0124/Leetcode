# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 1

        # print(isBadVersion(1))
        # print(isBadVersion(2))
        # print(isBadVersion(3))
        # print(isBadVersion(4))

        while left < right:
            mid = left + (right-left) // 2 
            for i in range(mid):
                if isBadVersion(mid):
                    right = mid
                else:
                    left = mid + 1
        
        return left
            



        