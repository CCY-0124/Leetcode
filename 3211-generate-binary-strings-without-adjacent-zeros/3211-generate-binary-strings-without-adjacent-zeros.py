class Solution(object):
    def validStrings(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def recur(cur_str,n): #recursion
            if len(cur_str) == n: #get a str with enough len
                res.append(cur_str) #add to answer list
                return #finish this route
            
            recur(cur_str+"1",n) #choice 1: add 1

            if cur_str == "" or cur_str[-1] == "1":
                recur(cur_str+"0",n) #choice 2: add 0 if empty string or last dig is 1
            
        recur("",n) #start from empty string

        return res
            
        