class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        k = dict(Counter(A))
        for ch in k.keys():
            if (k[ch] == (len(A)//2)):
                return ch
            

