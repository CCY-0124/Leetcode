class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_pointer = 0
        p_pointer  = 0 

        star = -1
        s_backup = -1

        if p.isalpha() and len(s) != len(p):
            return False
        
        while s_pointer < len(s):
            if p_pointer < len(p) and (p[p_pointer] == s[s_pointer] or p[p_pointer] == '?'):
                s_pointer += 1
                p_pointer += 1
                continue

            if p_pointer < len(p) and p[p_pointer] == '*':
                star = p_pointer
                s_backup = s_pointer
                if p_pointer == len(p) - 1:
                    return True
                p_pointer += 1
                continue

            if star != -1:
                p_pointer = star + 1
                s_backup += 1
                s_pointer = s_backup
                continue

            return False

        while p_pointer < len(p) and p[p_pointer] == "*":
            p_pointer += 1

        return p_pointer == len(p)
        




        