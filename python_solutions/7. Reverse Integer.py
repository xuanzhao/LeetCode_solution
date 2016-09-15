def reverse(x):
	"""
	:type x: int
	:rtype: int
	"""	
	
	if x >=0:
		pos = True	
	else: pos = False
	
	if not pos:
		x = -x	
		
	reverse = 0	
	while(x != 0):
		if reverse > 2**31 / 10 : return 0
		reverse = reverse * 10 + x % 10
		x /= 10	
	
	if pos:
		return reverse
	else: return -reverse