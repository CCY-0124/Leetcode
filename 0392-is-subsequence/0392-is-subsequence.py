class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if not s and not t or not s:
            return True

        if not t:
            return False

        first = 0
        second = 0
        while first < len(s) and second < len(t):
            if s[first] == t[second]:
                first += 1
            second += 1
            
        return first == len(s)

        