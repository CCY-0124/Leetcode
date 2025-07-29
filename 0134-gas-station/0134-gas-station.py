class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank_max = []
        for i in range(len(gas)):
            if i+1 >= len(gas):
                tank_max.append(gas[i]-cost[i]+gas[i+1-len(gas)])
            else:
                tank_max.append(gas[i]-cost[i]+gas[i+1])

        print(tank_max)

        if min(tank_max) < 0:
            return -1

        elif tank_max.count(max(tank_max)) > 1:
            return -1

        elif tank_max.count(max(tank_max)) == 1:
            return tank_max.index(max(tank_max))
