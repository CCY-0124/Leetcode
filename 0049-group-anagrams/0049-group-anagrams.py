class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [strs]

        ans = {}

        for i in strs:
            if "".join(sorted(i)) in ans:
                temp = ans["".join(sorted(i))]
                temp.append(i)
                ans["".join(sorted(i))] = temp
            else:
                ans["".join(sorted(i))] = [i]

        return [x for x in ans.values()]
        