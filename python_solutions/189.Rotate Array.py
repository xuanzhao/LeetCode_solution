def rotate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	
	def token(nums, k):
		while(k > 0):
			tl = nums.pop()
			nums.insert(0, tl)
			k -= 1
		
	token(nums, k)

def rotate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""

	p1 = nums[:-k]
	p2 = nums[-k:]

	a = p2 + p1
	for i in range(len(nums)):
		nums[i] = a[i]


def rotate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	new_nums = list(range(len(nums)))
	for i in range(len(nums)):
		new_nums[(i+k) % len(nums)] = nums[i]

	for i in range(len(nums)):
		nums[i] = new_nums[i]



def rotate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: void Do not return anything, modify nums in-place instead.
	"""

	def reverse(nums, start, end):
		while(start < end):
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1

	k = k % len(nums)
	reverse(nums,0, len(nums)-1)
	reverse(nums,0, k-1)
	reverse(nums,k, len(nums)-1)





