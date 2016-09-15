# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """

	left = 1
	right = n
	
	while left <= right:
		mid = (left + right) / 2
		num = guess(mid) 
		if num == 0: return mid
		elif num == -1: right = mid-1
		elif num == 1: left = mid + 1


def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """

	def loop(left, right):
		mid = (left + right) / 2
		num = guess(mid)
	
		if num == 0: return mid
		elif num == -1: return loop(left, mid-1)
		elif num == 1: return loop(mid+1, right)
	
	return loop(1, n)