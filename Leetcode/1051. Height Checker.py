class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sum = 0
        k = sorted(heights)
        for i in range(len(heights)):
            if (heights[i] != k[i]):
                sum +=1
        return sum