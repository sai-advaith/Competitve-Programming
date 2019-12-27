class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        sum = 0
        for ch in S:
            if ch in J:
                sum += 1
        return sum