class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                a = stack.pop()
                b = stack.pop()

                if tokens[i] == "+":
                    stack.append(b + a)
                elif tokens[i] == "-":
                    stack.append(b - a)
                elif tokens[i] == "*":
                    stack.append(b * a)
                else:
                    if b * a < 0 and b % a != 0: #either one is negative and being truncated
                        stack.append(b // a + 1)
                    else:
                        stack.append(b // a)

            else:
                stack.append(int(tokens[i]))

        return stack[-1]

        