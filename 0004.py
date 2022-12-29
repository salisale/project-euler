'''
4. Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

print(sorted([x*y for x in reversed(range(100,1000)) for y in reversed(range(100,1000)) if str(x*y)==str(x*y)[::-1]])[-1]) # = 906609

