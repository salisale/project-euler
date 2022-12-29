
'''
3. Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''

def isPrime(x): 
	if x%2==0 or x%3==0 or x%5==0 or x%7==0:
		return False

	for i in range(2, x):
		if x%i == 0:
			return False
	return True

x = 600851475143

# find factors
factors = []
for i in range(2, x):
	if x%i == 0:
		print(i, ' * ', int(x/i))
		if i in factors:
			break
		else:
			factors.append(i)
			factors.append(int(x/i))
		
list.sort(factors, reverse=True)
print('A list of factors in descending order of largeness: ', factors)

# find largest prime
answer = -1
for factor in factors:
	if isPrime(factor):
		answer = factor
		break

print(answer) # = 6857
