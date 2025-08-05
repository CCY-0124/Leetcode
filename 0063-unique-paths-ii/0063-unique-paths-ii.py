class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[-1][-1] == 1:
            return 0

        rows = [0] * (len(obstacleGrid[0])-1) + [1]
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        for i in range(n-1,-1,-1):
            temp = [0] * (m-1) + rows[-1:] if obstacleGrid[i][-1] != 1 else [0] * m

            for j in range(m-2,-1,-1):
                print(j)
                if obstacleGrid[i][j] != 1:
                    temp[j] = rows[j] + temp[j+1]
                else:
                    temp[j] = 0
            print(temp)
            rows = temp[:]
        
        return rows[0]
                
        