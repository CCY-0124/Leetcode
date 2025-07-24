class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        word = 'ab'

        if x > y:
            n = 1
            first, second = x, y
        else:
            n = -1
            second, first = x, y

        s = ''.join(list(s)[::n])

        ans = 0

        while word in s:
            index = s.find(word)

            if index != -1:
                ans += first
            s = s[:index]+s[index+2:]

        while word[::-1] in s:
            index = s.find(word[::-1])
            if index != -1:
                ans += second
            s = s[:index]+s[index+2:]

        return ans