class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 1
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        
        while n > 4:
            counter *= 3
            n -= 3

        counter *= n
        return counter
            
        