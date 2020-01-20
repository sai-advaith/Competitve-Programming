class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        mix = [0]*len(A)
        e = 0
        o = 1
        for i in A:
            if (i%2 == 0):
                mix[e] = i
                e += 2
            else:
                mix[o] = i
                o+=2
        return mix