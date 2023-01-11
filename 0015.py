'''
15. Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Visualisation: https://projecteuler.net/problem=15
'''

####################
# 1. For small grid, record all coordinates of possible paths and visualise answers (Proof of Concept)
####################

all_small_paths = [] # record all paths

def solve_small_grid(x,y,max_len,paths):
    paths = paths+[(x,y)]
    if x == max_len:
        solution = paths+[(x,j) for j in range(y+1,max_len+1)]
        all_small_paths.append(solution)
        return;
    elif y == max_len:
        solution = paths+[(i,y) for i in range(x+1, max_len+1)]
        all_small_paths.append(solution)
        return;
    else:
        solve_small_grid(x, y+1, max_len, paths)
        solve_small_grid(x+1, y, max_len, paths)

max_len = 4
solve_small_grid(1,1,max_len,[])

# print coordinates and visualise paths
for path in all_small_paths:
    out = ''
    for a in range(1, max_len+1):
        for b in range(1, max_len+1):
            out += '* ' if (a,b) in path else '  '
        out+='\n'
    print(path)
    print(out)
print("permutations for small grid %d x %d : %d" % (max_len-1, max_len-1, len(all_small_paths)))


'''
for grid 3x3, should print:
[(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 4)]
* * * *
      *
      *
      *

[(1, 1), (1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 4)]
* * *
    * *
      *
      *

[(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (4, 4)]
* * *
    *
    * *
      *
...

permutations : 20
'''


####################
# 2. For high-n grid e.g. 20x20, keep only counts
####################
count = 0
def solve_giant_grid(x,y, max_len):
    if x == max_len or y == max_len:
        return 1
    else:
        x_count = solve_giant_grid(x,y+1,max_len)
        y_count = solve_giant_grid(x+1,y,max_len)
        return x_count+y_count
#answer = solve_giant_grid(4,4, 10)
#print("permutations for giant grid %d x %d : %d" % (max_len-1, max_len-1, answer) # 

# Unfortunately, this takes forever..... !!


####################
# 3. Viable solution: don't iterate through all possible paths, do a fibo-like operation on matrix
####################

n = 23
distMap = [([0]*n) for i in range(0,n)]
distMap[0][0] = 0
distMap[0][1] = 1
distMap[1][0] = 0
distMap[1][1] = 1

for i in range(1,n):
    for j in range(1,n):
        distMap[i][j] = distMap[i][j-1] + distMap[i-1][j]

for arr in distMap: # print matrix
    print('  '.join([str(a) for a in arr])+'\n')

print('Grid 3x3 has %d possible paths'%distMap[4][4]) # 20
print('Grid 5x5 has %d possible paths'%distMap[6][6]) # 252
print('Grid 20x20 has %d possible paths'%distMap[21][21]) # 137846528820


