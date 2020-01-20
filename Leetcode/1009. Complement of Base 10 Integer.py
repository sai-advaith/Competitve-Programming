class Solution:
    def bitwiseComplement(self, N: int) -> int:
            k = bin(N).replace("0b","")
            s = ""
            for ch in k:
                if ch == '1':
                    s = s + '0'
                else:
                    s = s + '1'
            return int(s,2)