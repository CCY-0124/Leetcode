class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        richest = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > richest:
                richest = sum(accounts[i])

        return richest

        