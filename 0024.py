'''
24. Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def permute(arr):
	if len(arr) == 2:
		return [''.join(arr), ''.join(reversed(arr))]
	else:	
		out = []
		for x in permute(arr[1:]): # tail
			for i in range(0, len(x)+1):
				out.append(x[:i]+arr[0]+x[i:])
		return out


perm = permute(['0','1','2','3','4','5','6','7','8','9'])
print(sorted(perm)[999999]) # 2783915460