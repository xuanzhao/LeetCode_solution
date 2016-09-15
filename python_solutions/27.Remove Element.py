def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    nums.sort()

    illeg , n = 0, 0

    for x in nums:
    	if x < val:
    		n += 1
    	elif x == val:
    		n += 1
    		illeg += 1
    	else:
    		n += 1
    		if illeg >0:
				nums[n-illeg-1] = x
				nums[n-1] = None

    return n-illeg



def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    i = 0
    for j in range(len(nums)):
    	if nums[j] != val:
    		nums[i] = nums[j]
    		i += 1

    print nums
    return i



def removeElement(nums, val):

	i = 0
	n = len(nums)
	while(i < n):
		if nums[i] == val:
			nums[i] = nums[n]
			n -= 1
		else:
			i += 1

	return n







