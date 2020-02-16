class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        a = []
        cnt = Counter()
        A = A + " " + B
        A = A.split(" ")
        for word in A:
            cnt[word] += 1
        for k in cnt:
            if(cnt[k] == 1):
                a.append(k)
        return a