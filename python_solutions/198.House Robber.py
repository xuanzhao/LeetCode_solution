
def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	def get_max(results):

		max_int = 0

		for item in results:
			if sum(item) > max_int:
				max_int = sum(item)

		return max_int

	def loop(acc, rest):
		#if rest == []: results.append(acc); return


		new_acc = acc + [rest[0]]
		if rest[1:] != []:
			loop(acc, rest[1:])
		else: 
			results.append(acc)
			results.append(new_acc)
		if rest[2:] != []:
			loop(new_acc, rest[2:])
		else: results.append(new_acc)


	results = []

	for i in range((len(nums)+1)/2):
		loop([], nums[i:])

	print results

	return get_max(results)


          



def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	#S[i] = max(S[i-2], S[i-3]) + A[i]

    n = len(nums)
    if n==0:
        return 0;
    if n == 1:
        return nums[0]
    s = [0]*(n+1)
    s[1] = nums[0]
    s[2] = nums[1]
     
    for i in range(3,n+1):
        s[i] = (max(s[i-2],s[i-3]) + nums[i-1])
    return max(s[n],s[n-1])



def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	#dp[i] = max(num[i] + dp[i - 2], dp[i - 1])
	
	n = len(nums)
	if n == 0: return 0
	elif n == 1: return nums[0]
	
	dp = [0] * (n)
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])
	
	for i in range(2, n):
		dp[i] = max(nums[i] + dp[i-2], dp[i-1])
	
	return dp[-1]


def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	a, b = 0, 0
	for i in range(len(nums)):
		if (i % 2 ==0):
			a += nums[i]
			a = max(a,b)
		else:
			b += nums[i]
			b = max(a,b)

	return max(a,b)


def rob(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""

	a, b = 0, 0

	for i in range(len(nums)):
		m, n = a, b
		a = n + nums[i]
		b = max(m, n)

	return max(a,b)


	


















