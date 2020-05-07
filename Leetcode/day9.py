class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def back(s):
            arr = []
            j = 0
            for ch in s:
                if ch == '#' and len(arr) != 0:
                    arr = arr[:-1]
                    j = j -1
                elif ch!='#':
                    arr.append(ch)
                    j+=1
            r = ''.join(arr)
            return r
        return (back(S) == back(T))