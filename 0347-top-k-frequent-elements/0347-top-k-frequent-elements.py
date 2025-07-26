class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fre_dict = {}
        max_fre = []

        for i in range(len(nums)):
            fre_dict[nums[i]] = fre_dict.get(nums[i], 0) +1

        for index, value in fre_dict.items():
            max_fre.append([value,index])

        max_fre = sorted(max_fre)[::-1]

        return [x[1] for x in max_fre[:k]]



        