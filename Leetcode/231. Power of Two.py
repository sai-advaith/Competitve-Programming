class Solution(object):
    def isPowerOfTwo(self,n):
            if n <= 0:
                return False
            else:
                return (n & (-n) == n)