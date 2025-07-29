class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        if s == 0:
            return 0

        g.sort()
        s.sort()
        counter = 0

        pointer = 0

        for i in range(len(s)):
            if counter < len(g):
                if s[i] >= g[pointer]:
                    counter +=1
                    pointer +=1

            else:
                return counter
        
        return counter


        