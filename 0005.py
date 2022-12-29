'''
5. Small Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# 1-10
print(1*2*2*3*5*7*2*3) # = 2520

# 1-20
print(1*2*2*3*5*7*2*3*11*13*2*17*19) # = 232792560

# no algorithm.. this can be eyeballed: they are a list of most minimum collection of factors needed to produce all numbers from 1-20, either by itself or by multiplication e.g. 4 of 2's produce 16
