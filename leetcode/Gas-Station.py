class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        \\\
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        \\\
        total_tank = 0
        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        return start_index if total_tank >= 0 else -1
