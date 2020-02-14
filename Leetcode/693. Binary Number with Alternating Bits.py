class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n).split('0b')[1]
        for i in range(0,len(n)-1):
            if n[i] == n[i+1]:
                return False
        return True