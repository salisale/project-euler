
import math

def isPrime(x):
	if x <= 5: return True if x in (2,3,5) else False
	if x%2==0 or x%3==0 or x%5==0 : return False
	for i in range(2, math.ceil(x/2)):
		if x%i==0:
			return False
	return True
