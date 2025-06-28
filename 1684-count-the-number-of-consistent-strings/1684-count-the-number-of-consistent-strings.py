class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        n = range(len(words))
        for i in n:
            if set(words[i]).issubset(set(allowed)):
                count+=1

        return count
        