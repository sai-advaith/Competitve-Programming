class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, current_gas, total_gas =0, 0, 0
        for index in range(len(gas)):
            diff = gas[index] - cost[index]
            total_gas += diff
            current_gas += diff
            
            if current_gas < 0:
                start = index + 1
                current_gas = 0
                
        if total_gas >= 0:
            return start
        return -1