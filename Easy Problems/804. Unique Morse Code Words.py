def uniqueMorseRepresentations(words):
    l = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    str = []
    for k in words:
        s = ""
        for ch in k:
            s = s + l[ord(ch) - 97]
        str.append(s)
    return (len(set(str)))
print(uniqueMorseRepresentations(["rwjje","aittjje","auyyn","lqtktn","lmjwn"]))