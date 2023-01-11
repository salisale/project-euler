
def run():
	allMap = {}
	x = 10000
	currPos = 1
	nums = [i for i in range(1, x)]
	nos = {}

	for x in reversed(range(500000, 1000000)):
		count = 0
		seq = []
		while x != 1:
			if x in nos:
				nos[x] = count+nos[x]
				break
			else:
				if x%2 == 0:
					x = x/2
				else:
					x = 3*x + 1
			#print('new x is ...', x)
			count += 1
			seq.append(int(x))

		#print(seq)
		#print(count)
		for i in range (0,len(seq)):
			num = seq[i]
			if num < len(nums):
				if count - i > nos.get(num, 0):
					nos[num] = count - i

	print(nos)

def check(x):
	count = 0
	seq = []
	while x != 1:
		if x%2 == 0:
			x = x/2
		else:
			x = 3*x + 1
		#print('new x is ...', x)
		count += 1
		seq.append(int(x))
	print(seq)
	print(len(seq))

check(9365)