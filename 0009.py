'''
9. Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math

def findSum(xy_sum,total_sum):
	tups = [] # a, b, c
	for i in range(0,math.ceil(xy_sum/2)):
		a,b,c = total_sum-xy_sum, xy_sum-i, i
		if a > b: # filter out 400,400,200
			tups.append((a,b,c))
	return tups

def findTripletSum(total_sum):
	triplets = []
	for i in reversed(range(0, total_sum)):
		triplets += findSum(i, total_sum)
	return triplets

triplets = findTripletSum(1000)
#print(triplets)

for tup in triplets:
	if tup[0]**2==tup[1]**2+tup[2]**2:
		print(tup, ' => ', math.prod(tup)) # = (425,375,200) => 31875000
 