def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""
	dic = {}
	maxStr = ''
	
	for i, c in enumerate(s):
		if not dic.get(c): 
			dic[c] = i
			maxStr = maxStr + c
		else:
			dic[c] = i
			seq = dic[c]
			if seq[-1] - seq[-2] > len(maxStr):
				maxStr = s[seq[-2]:seq[-1]]
		print maxStr
	return len(maxStr)


def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""

	dic = {}
	maxLen = 0
	curLen = 0

	for i, c in enumerate(s):
		if not dic.get(c):
			dic[c] = [i]
			curLen += 1
		else:
			dic[c].append(i)
			seqlen = (dic[c][-2],dic[c][-1])
			print seqlen, seqlen[1]-seqlen[0]
			if seqlen[1]-seqlen[0] > maxLen and \
				seqlen[1]-seqlen[0] > curLen:
				maxLen = seqlen[1] - seqlen[0]
			elif curLen > maxLen:
				maxLen = curLen 
			curLen = 1

		print maxLen, curLen

	maxLen = curLen if curLen > maxLen else maxLen


	return maxLen



def lengthOfLongestSubstring(s):
	"""
	:type s: str
	:rtype: int
	"""

	i, j = 0, 0

	dic = {}
	maxLen = 0

	while(i < len(s) and j < len(s)):
		if not dic.get(s[j]):
			dic[s[j]] = True
			maxLen = max(maxLen, j-i+1)
			j += 1
		elif dic[s[j]]:
			maxLen = max(maxLen, j-i)
			dic[s[i]] = False
			i += 1


	return maxLen































