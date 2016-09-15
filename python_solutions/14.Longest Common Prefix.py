def longestCommonPrefix( strs):
	"""
	:type strs: List[str]
	:rtype: str
	"""
	
	if strs == []: return ""
	elif len(filter(lambda x: x=='', strs)) > 0: return ""
	elif len(strs) == 1: return strs
	
	first_cs = map(lambda x: x[0], strs)
	has_b = reduce(lambda x,y: x if x==y else False, first_cs)
	if has_b == False: return ""
	
	base = reduce(lambda x,y: x if len(x) < len(y) else y, strs)
	rest = strs
	rest.remove(base)
	
	lcp = ""
	def loop(base, i):
		if i == 0: return ""
		elif len(filter(lambda s: base in s[:i], rest)) == len(rest):
			return base
		else:
			i -= 1
			return loop(base[:i], i)
	
	lcp = loop(base, len(base))
	
	return lcp