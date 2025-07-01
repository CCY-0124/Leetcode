class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        reverse = []
        for i in range(len(word)):
            reverse.append(word[i])
            if word[i] == ch:
                return "".join(reverse[::-1]+list(word[i+1:]))
        
        return word

                

        