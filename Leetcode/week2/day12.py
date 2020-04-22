class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        j =0 
        for i in range(len(stones)-1):
            stones = sorted(stones,reverse=True)
            if stones[j] == stones[j+1]:
                stones = stones[j+2:]
            else:
                k = stones[j] - stones[j+1]
                stones = stones[j+2:]
                stones = [k] + stones
            if len(stones) == 1 or len(stones) == 0:
                break
        if stones == []:
            return 0
        else:
            return stones[0]