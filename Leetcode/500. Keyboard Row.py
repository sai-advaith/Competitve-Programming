def findWords(words):
	r1 = ['q','w','e','r','t','y','u','i','o','p']
	r2 = ['a','s','d','f','g','h','j','k','l']
	r3 = ['z','x','c','v','b','n','m']
	k = 0
	s = []
	r = []
	g = True
	for i in words:
		i = (i.lower())
		if i[0] in r1:
			k = 1
		elif i[0] in r2:
			k = 2
		elif i[0] in r3:
			k = 3
		for ch in range(1,len(i)):
			if k == 1:
				g = g and (i[ch] in r1)
			elif k == 2:
				g = g and (ch in r2)
			elif k == 3:
				g= g and (ch in r3)
			print(g)
		s.append(g)
	for i in range(len(s)):
		if (s[i]):
			r.append(words[i])
	return r
print(findWords(["Hello","Alaska","Dad","Peace"]))