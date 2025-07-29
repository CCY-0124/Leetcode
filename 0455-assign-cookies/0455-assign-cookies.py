class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort()
        res = 0
        for kid in g:
            if s and kid <= s[-1]:
                res += 1
                s.pop()
            if not s or kid < s[0]:
                return res

        return res
        