class Solution:
    def maximum69Number (self, num: int) -> int:
        a = list(str(num))
        s = [num]
        for i in range(len(a)):
            if(a[i] == '6'):
                a[i] = '9'
            else:
                a[i] = '6'
            s.append(int("".join(a)))
            a = list(str(num))
        d = s[0]
        for i in s:
            if (i>d):
                d = i
        return d