def moveZeroes(nums):
    """
	:type nums: List[int]
	:rtype: void Do not return anything, modify nums in-place instead.
	"""
	
	count = 0
	
	for i,n in enumerate(nums):
		if n == 0: count += 1
		else:
			nums[i - count] = n
	
	if count != 0: nums[-count:] = [0] * count

]