class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        k = []
        for word in s:
            k.append(word[::-1])
        return (" ".join(k))