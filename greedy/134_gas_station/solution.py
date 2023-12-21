from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        index = 0
        while index < n:
            if cost[index] > gas[index] or (
                index > 0
                and cost[index] == cost[index - 1]
                and gas[index] == gas[index - 1]
            ):
                index += 1
                continue
            can_travel = True
            tank = 0
            for i in range(n):
                tank += gas[(index + i) % n]
                if tank < cost[(index + i) % n]:
                    can_travel = False
                    break
                tank -= cost[(index + i) % n]
            if can_travel:
                return index

            index += 1
        return -1

    def canCompleteCircuit_greedy(self, gas: List[int], cost: List[int]) -> int:
        """Question states the solution will be unique.
        Consider:
            7 6 0 11 4
            5 4 9  2 5

        If starting from 0 fails at 2, it is useless to try again 1, since by the
        time it reached 1 when starting from 0, the tank would have be at >= 0 so
        there's not way to get a better result starting at 1.
        """
        n = len(gas)
        total_surplus = 0
        tank = 0
        start = 0
        for i in range(n):
            total_surplus += gas[i] - cost[i]
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                start = i + 1
        if total_surplus >= 0:
            return start
        return -1
