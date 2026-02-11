class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        lrdict = {"L":0,"R":0}

        for i in range(len(s)):
            if s[i] == "L":
                lrdict["L"] += 1
            else:
                lrdict["R"] += 1
        
            if lrdict["L"] == lrdict["R"]:
                res +=1
                lrdict = {"L":0,"R":0}
            
        return res

        