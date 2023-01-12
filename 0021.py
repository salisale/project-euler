'''
21. Amicable numbers

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
import math

def findFactors(x):
	out = [1] # including 1
	for i in range(2,math.floor(x**0.5)+1): # but excluding n
		if x%i == 0:
			out += list(set([i, int(x/i)]))
	return out

amicNums = []
facMap = dict()
for i in range(2,10000):
	facSum = sum(findFactors(i))
	facMap[i] = facSum
	if i == facMap.get(facSum, 0) and i != facSum:
		amicNums += [i, facSum]

print(amicNums)
print(sum(amicNums)) # 31626