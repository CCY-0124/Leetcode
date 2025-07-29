class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tank_max = []
        for i in range(len(gas)):
                tank_max.append(gas[i]-cost[i])

        if sum(tank_max) < 0:
            return -1

        print(tank_max)
        print(sum(tank_max))

        start = 0
        tank = 0
        total = 0

        for i in range(len(tank_max)):
            tank += tank_max[i]
            total += tank_max[i]

            if tank < 0:
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
