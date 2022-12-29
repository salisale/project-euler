
'''
3. Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''
from helper import isPrime

x = 600851475143

# find factors
factors = []
for i in range(2, int(x**0.5)): # 2 -> sqrt(x)
	if x%i == 0:
		print(i, ' * ', int(x/i))
		factors.append(i)
		factors.append(int(x/i))

list.sort(factors, reverse=True)
print('A list of factors in descending order of largeness: ', factors)

# find largest prime
print([x for x in factors if isPrime(x)][0]) # = 6857
