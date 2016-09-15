def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    
    if len(s) != len(t): return False
	dic = {}
	
	for c in s:
		if not dic.get(c):
			dic[c] = 1
		else:
			dic[c] += 1
	
	for c in t:
		if not dic.get(c): return False
		else: 
			dic[c] -= 1
			if dic[c] < 0: return False
	
	return True