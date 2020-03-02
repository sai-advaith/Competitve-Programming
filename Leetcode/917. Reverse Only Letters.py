class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        char_pos = []
        letter = []
        for i in range(len(S)):
            if S[i].isalpha():
                letter.append(S[i])
            else:
                char_pos.append(i)
        s = ""
        j = 0
        k = len(letter)-1
        for i in range(len(S)):
            if(j < len(char_pos) and i==char_pos[j]):
                s = s + S[i]
                j+=1
            else:
                s = s + letter[k]
                k = k - 1
        return s