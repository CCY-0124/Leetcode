class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "{":
                stack.append("}")
            elif i == "[":
                stack.append("]")
        
            else:
                if i != stack[-1] or not stack:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False