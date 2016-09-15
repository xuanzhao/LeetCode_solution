
import pdb

def convert(s, numRows):
	"""
	:type s: str
	:type numRows: int
	:rtype: str
	"""
	
	if numRows==1: return s

	length = 2*numRows - 2
	
	row, col = 0, 0
	count = 0
	nrow = numRows
	bcol = length - nrow + 1

	n = 1
	while True:
		if n*length >= len(s):
			break
		else: n+=1

	ncol = bcol * n
	dp = [None] * (nrow * ncol) 
	
	while True:
		#pdb.set_trace()
		for i in range(nrow):
				pos = row * ncol + col
				dp[pos] = s[count]  
				count += 1
				row += 1
				if count == len(s):
					return ''.join(filter(lambda x: x!=None, dp))
		row -= 1		
		for i in range(length-nrow):
			row -= 1
			col += 1
			pos = row * ncol + col
			dp[pos] = s[count]
			count += 1
			if count == len(s):
				return ''.join(filter(lambda x: x!=None, dp))		
		row -= 1
		col += 1

	# time exceeded

def convert(s, numRows):
	"""
	:type s: str
	:type numRows: int
	:rtype: str
	"""
	
	if numRows==1: return s

	length = 2*numRows - 2


	res = []

	for i in range(numRows):
		for j in range(i, len(s), length):
			res.append(s[j])
			tmp = j + length - 2 * i
			if (i != 0 and i != numRows-1 and tmp < len(s)):
				res.append(s[tmp])

	return ''.join(res)
