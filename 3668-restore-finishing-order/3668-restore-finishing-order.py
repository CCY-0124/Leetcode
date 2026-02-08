class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        res = []
        for i in order:
            if i in friends:
                res.append(i)
        return res
        