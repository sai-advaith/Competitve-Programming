class Solution:
    def toGoatLatin(self, S: str) -> str:
        k = S.split(" ")
        r = []
        for i in range(len(k)):
            if (k[i][0].lower() in ['a','e','i','o','u']):
                r.append(k[i])
            else:
                r.append(k[i][1:len(k[i])]+k[i][0])
            r[i] += "ma"+'a'*(i+1)
        return " ".join(r)