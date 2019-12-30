class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def selfDividing(num):
            g = True
            k = num
            while (num > 0):
                r = num % 10
                if (r!= 0 and k % r  != 0):
                    g = False
                    break
                num //= 10
            return g
        arr = []
        for i in range(left,right+1):
            if (selfDividing(i) and '0' not in str(i)):
                arr.append(i)
        return arr
    
            