class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change_dict = {5:0,10:0,20:0}

        for i in range(len(bills)):
            print(change_dict)
            change_dict[bills[i]] = change_dict.get(bills[i], 0) + 1

            if bills[i] == 10:
                if change_dict[5] > 0:
                    change_dict[5] -= 1
                else:
                    return False

            if bills[i] == 20:
                if change_dict[10] > 0 and change_dict[5] > 0:
                    change_dict[5] -= 1
                    change_dict[10] -= 1
                elif change_dict[5] > 2:
                    change_dict[5] -= 3
                else:
                    return False

        return True





        