class Solution:
    def findComplement(self, num: int) -> int:
        num =bin(num).replace("0b","")
        str = ""
        for ch in num:
            if ch == '0':
                str = str+'1'
            else:
                str = str + '0'
        return int(str,2)