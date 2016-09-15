def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    n, sim = 0, 0

    current = None
    for x in nums:
    	n += 1
    	if current != x:
    		current = x
    		nums[n-sim-1] = current
    	else:
    		sim += 1

    return n-sim



def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 0 return 0:
    i = 0
    for j in range(1, len(nums)):
    	if nums[j] != num[i]:
    		i += 1
    		nums[i] = nums[j]

    return i+1 

