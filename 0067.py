'''
67. Maximum path sum II

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

		3
	   7 4
      2 4 6
     8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''


#################################################
# Note: copy pasta from Problem 18 - 0018.py
#################################################

# Final optimised algorithm, instead of keeping a list of all candidates like
#    [0]
#   [1,2] => 	[[1],[2]]
#  [3,4,5] => [[4],[5,6],[7]]
#  ...
# The overlapping candidates i.e. [5,6] will encounter all of the same sequence of integers, therefore we can do max([5,6]) and render each intermediate step simply as e.g. [4,6,7]


with open("files/p067_triangle.txt", "r") as f:
    file = f.readlines()

print(file)
matrix = [x.split() for x in file]
print(matrix)

output = [int(matrix[0][0])]
for i in range(1,len(matrix[-1])):
	next_row = matrix[i]
	right_overlap = 0
	downward_sum = []
	for j in range(0,len(output)): # iterate through output so far
		next_left, next_right = int(next_row[j]), int(next_row[j+1])
		left_overlap = output[j]+next_left
		downward_sum.append(max(left_overlap,right_overlap))
		right_overlap = output[j]+next_right
	downward_sum.append(right_overlap) # add last trailing value
	output = downward_sum
	print('i=',i,' output=',output)

print(output) 
print(max(output)) # 7273