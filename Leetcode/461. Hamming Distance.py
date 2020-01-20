class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = list(bin(x).replace("0b",""))
        y = list(bin(y).replace("0b",""))
        a = len(x)
        b = len(y)
        x = b * ['0'] + x
        y = a * ['0'] + y
        sum = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                sum = sum + 1
        return sum