class Solution:
    def balancedStringSplit(self,s):
        c = 0
        sum = 0
        for ch in s:
            if ch == 'R':
                sum = sum + 1
            if ch == 'L':
                sum = sum - 1
            if sum == 0:
                c = c + 1
        return c

    
        