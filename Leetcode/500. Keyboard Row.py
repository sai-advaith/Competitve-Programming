class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        r1 = ['q','w','e','r','t','y','u','i','o','p']
        r2 = ['a','s','d','f','g','h','j','k','l']
        r3 = ['z','x','c','v','b','n','m']
        k = 0
        s = []
        def checkRow(s,k):
            for ch in s:
                if k == 1 and ch not in r1:
                    return False
                elif k == 2 and ch not in r2:
                    return False
                elif k == 3 and ch not in r3:
                    return False
            return True
        for i in words:
            d = (i.lower())
            if d[0] in r1:
                k = 1
            elif d[0] in r2:
                k = 2
            elif d[0] in r3:
                k = 3
            if (checkRow(d,k)):
                s.append(i)
        return s