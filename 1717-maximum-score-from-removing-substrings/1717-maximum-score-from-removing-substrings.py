class Solution(object):
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """

        if x > y:
            first, second = x, y
            n = 1
            string = 'ab'
            
        else:
            second, first = x, y
            n = 1
            string = 'ba'

        ans = 0
        stack = []
        print(s[::n])

        for word in s[::n]:
            if stack and stack[-1] == string[0] and word == string[1]:
                stack.pop()
                
                ans += first
                print(ans)

            else:
                stack.append(word)
        
        remain = "".join(stack)
        print(remain)
        stack = []

        for word in remain[::n]:
            if stack and stack[-1] == string[1] and word == string[0]:
                stack.pop()
                ans += second
                print(ans)

            else:
                stack.append(word)

        return ans