class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left = 0
        for pos, amt in shift:
            if pos == 0:
                left = left + amt
            else:
                left -= amt
        left = left % len(s)
        return s[left:] + s[:left]