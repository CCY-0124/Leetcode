class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels = set(jewels)
        count = 0
        stones = list(stones)

        for i in range(len(stones)):
            if stones[i] in jewels:
                count +=1
        
        return count

        