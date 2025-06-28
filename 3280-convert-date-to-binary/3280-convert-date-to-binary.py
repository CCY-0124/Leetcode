class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        date = date.split("-")
        for i in range(len(date)):
            date[i] = format(int(date[i]),'b')
        
        return "-".join(date)
        