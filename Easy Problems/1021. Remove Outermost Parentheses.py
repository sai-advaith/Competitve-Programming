class Solution:
    def removeOuterParentheses(self, S: str) -> str:
            sum = 0
            k = list(S)
            j = 0
            for i in range(len(k)):
                if k[i] == '(':
                    sum  +=1
                if k[i] == ')':
                    sum -= 1
                if sum == 0:
                    k[j] = ''
                    k[i] = ''
                    j = i+1
            return "".join(k)