def isPowerOfThree(n):
	"""
	:type n: int
	:rtype: bool
	"""
	
	def loop(n):
		if n <= 3: return n
		else: return loop(n / 3.0)
	
	if n<=0: return False
	elif n==1: return True
	
	v = loop(n)
	if v % 3 == 0: return True
	else: return False


	def loop(n):

		if n and n % 3 == 0: return loop(n / 3)

		return n ==1

	return loop(n)

	

    