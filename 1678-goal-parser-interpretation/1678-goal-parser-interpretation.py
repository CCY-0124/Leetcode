class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        pointer = 0
        ans = []
        while pointer < len(command):
            if command[pointer:pointer+ 2] == "()":
                ans.append("o")
                pointer += 2
            elif command[pointer:pointer+ 4] == "(al)":
                ans.append("al")  
                pointer += 4  
            else:
                ans.append("G") 
                pointer += 1

        return "".join(ans)

        