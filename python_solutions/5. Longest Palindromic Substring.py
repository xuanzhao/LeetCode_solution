def longestPalindrome(s):
	"""
	:type s: str
	:rtype: str
	"""
	
	## 0 1 2   3   4 5 6 
	## s is odd, mid = len(s) // 2 , l = mid-1, r = mid+1
	## 0 1 2 3   -1    4 5 6 7
	## s is even, mid = len(s) // 2, l = mid-1, r = mid+1
	
	## This is a wrong solution, like case 'abacaaaaaaa'
	def loop(s, maxStr):
		mid = len(s) // 2
		l = mid-1
		r = mid+1
		
		if len(s) % 2 ==0:
			subStr = ''
		else:
			subStr = s[mid]
		
		while(l>-1 and r <len(s)):
			if s[l] == s[r]:
				subStr = s[l] + subStr + s[r]
				l -= 1
				r += 1
			else:
				break

		if len(subStr) > len(maxStr):
				maxStr = subStr
				lis.append(maxStr)
				print maxStr, subStr

		if len(s) > 2:
			if len(subStr) < len(s[: mid+1]):
				loop(s[: mid+1], maxStr)
			if len(subStr) < len(s[mid:]):
				loop(s[mid:], maxStr)

	if len(s) <=1: return s
	elif len(s) == 2: return s[0]

	maxStr = ''
	lis = []
	loop(s, '')
	print lis
	for s in lis:
		if len(s) > len(maxStr):
			maxStr = s

	return maxStr



def longestPalindrome(s):
	"""
	:type s: str
	:rtype: str
	"""

	def expandAroundCenter(s, l, r):
		L = l; R = r
		while(L >= 0 and R < len(s)):
			if s[L]== s[R]:
				L -=1
				R +=1

		return R-L-1
		
	start = 0; end = 0
	for i in range(1,len(s)):
		len1 = expandAroundCenter(s, i, i)
		len2 = expandAroundCenter(s, i, i+1)
		lens = max(len1, len2)
		
		print len1, len2, lens
		if (lens > end - start):
			start = i - (lens+1) // 2
			end = i + lens // 2
	
	return s[start: end+1]


def longestPalindrome(s):
	"""
	:type s: str
	:rtype: str
	"""

	maxst = 0
	maxlen = 0
	dp ={}

	for i in range(len(s)):
		dp[i,i] = True
		maxst = i
		maxlen = 1

	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			dp[i,i+1] = True
			maxst = i
			maxlen = 2

	for l in range(3, len(s)+1):
		for i in range(len(s)-l+1):
			j = i + l -1
			if s[j] == s[i] and dp.get((i+1, j-1)):
				dp[i,j] = True
				maxst = i
				maxlen = l

	print maxst, maxlen
	return s[maxst:maxst+maxlen]


def longestPalindrome(s):
	"""
	:type s: str
	:rtype: str
	"""
	maxst = 0
	maxlen = 0
	dp = [0] * len(s)*len(s)

	for i in range(len(s)):
		dp[i + i * len(s)] = True
		maxst = i
		maxlen = 1

	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			dp[i+1 + i*len(s)] = True
			maxst = i
			maxlen = 2

	for l in range(3, len(s)+1):
		for i in range(len(s)-l+1):
			j = i + l -1
			if s[j] == s[i] and dp[len(s)*(i+1) + j-1]:
				dp[i*len(s)+j] = True
				maxst = i
				maxlen = l

	print maxst, maxlen
	return s[maxst:maxst+maxlen]









