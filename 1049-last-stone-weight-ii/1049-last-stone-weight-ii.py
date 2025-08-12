class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        total_sum = sum(stones)
        
        target_sum = total_sum //2

        dp =[[False] * (target_sum + 1) for _ in range(len(stones) + 1)]

        for i in range(len(stones) + 1):
            dp[i][0] = True
        
        for i in range(1, len(stones) + 1):
            for j in range(1, target_sum + 1):
                if j < stones[i - 1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]

        for i in range(target_sum, -1, -1):
            if dp[len(stones)][i]:
                return total_sum - 2 * i
        
        return dp[len(stones)][target_sum]
        