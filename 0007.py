'''
7. 10001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''

from helper import isPrime

count = 0
x = 1

while count < 10001:
	if isPrime(x):
		count += 1
	x += 1

print(x-1) # = 104743