'''
2. Even fibo no

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

fib = [1,2]

while fib[-2]+fib[-1] < 4000000:
	fib.append(fib[-1]+fib[-2])

print(sum([x for x in fib if x%2==0])) # = 4613732
