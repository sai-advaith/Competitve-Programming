class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        k = dict(Counter(nums))
        for val in k.keys():
            if k[val] == 1:
                return val
            