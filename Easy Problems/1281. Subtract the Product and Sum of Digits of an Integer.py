class Solution:
    def subtractProductAndSum(self,n: int) -> int:
        sum = 0
        product = 1
        for ch in str(n):
            sum = sum + int(ch)
            product = product*int(ch)
        return (product-sum)