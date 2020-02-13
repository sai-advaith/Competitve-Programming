def countPrimeSetBits(L, R):
	counter = 0
	def countPrime(a):
		c = 0
		for ch in a:
			if ch == '1':
				c = c + 1
		return isPrime(c)
	def isPrime(k):
		c = 0
		for i in range(1,k):
			if (k%i == 0):
				c = c + 1
		return (c==1)
	for i in range(L,(R+1)):
		i = bin(i).split('0b')[1]
		if countPrime(i):
			counter = counter + 1
	return counter
print(countPrimeSetBits(10,15))