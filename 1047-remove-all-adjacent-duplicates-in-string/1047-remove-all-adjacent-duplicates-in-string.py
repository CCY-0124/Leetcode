class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for i in s:
            if not stack:
                stack.append(i)
            elif i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)

        return "".join(stack)

        