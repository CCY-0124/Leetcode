class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        letter_dict = {}
        for i in range(len(s)):
            if s[i] in letter_dict:
                letter_dict[s[i]][1] = i
            else:
                letter_dict[s[i]] = [i,0]

        letter_list = sorted([x for x in letter_dict.values()])

        index = []
        max_index = 0
        min_index = 0

        for i in range(len(letter_list)):
            if letter_list[i][0] > max_index:
                index.append([min_index,max_index])
                print(max_index,min_index)
                min_index = letter_list[i][0]
                max_index = max(letter_list[i][1],max_index)

            else:
                max_index = max(letter_list[i][1],max_index)
                min_index = min(letter_list[i][0],min_index)

        index.append([min_index,len(s)-1])

        print(index)

        res = []
        for i in range(len(index)):
            if index[i][1]-index[i][0]+1 <= 0:
                res.append(1)
            else:
                res.append(index[i][1]-index[i][0]+1)

        return res
            
            

            



