class Solution:   
    def isHappy(self, n: int) -> bool:
        def sum_nums(n):
            sum = 0
            while n>0:
                r = n%10
                sum += r*r
                n//=10
            return sum
        s1 = n
        f1 = n
        while True:
            s1 = sum_nums(s1)
            f1 = sum_nums(sum_nums(f1))
            if (s1 != f1):
                continue
            else:
                break
        return s1 == 1