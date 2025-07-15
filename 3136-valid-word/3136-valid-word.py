class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        checker = [ x.lower() for x in word if x.isalpha() or x.isdigit()]
        alpha_checker = set([ x.lower() for x in word if x.isalpha()])
        checker_set = set(checker)
        vowel = set(['a', 'e', 'i', 'o', 'u'])
        if len(word) < 3:
            return False
        elif len(word) != len(checker):
            return False
        elif not alpha_checker&vowel:
            return False
        elif not alpha_checker-vowel:
            return False
        
        return True

        