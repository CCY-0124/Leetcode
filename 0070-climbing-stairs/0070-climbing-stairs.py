class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        a = 1
        b = 2
        for i in range(2,n):
            a, b = b, a+b
        
        return b
        