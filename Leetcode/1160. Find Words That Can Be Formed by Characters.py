class Solution:
    def countCharacters(self,words, chars):
        from collections import Counter
        c = dict(Counter(chars))
        def present(word,c):
            k = c.copy()
            g = True
            for ch in word:
                if ch in list(k.keys()) and k[ch] > 0:
                    k[ch] = k[ch] - 1
                else:
                    g = False
                    break
            return g
        sum = 0
        for str in words:
            if present(str,c):
                sum = sum + len(str)
        return sum