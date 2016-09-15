# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
	
	def recur(left, right):
		if left == right: return left
		else: mid = (left + right) / 2
		
		if isBadVersion(mid):
			return recur(left, mid)
		else: return recur(mid+1, right)
	
	return recur(1, n)

def firstBadVersion(n):
	"""
	:type n: int
	:rtype: int
	"""
	
	left = 1
	right = n
	
	while(left != right):
		mid = (left + right) /2
		if isBadVersion(mid):
			right = mid
		else: left = mid + 1
	
	return left

