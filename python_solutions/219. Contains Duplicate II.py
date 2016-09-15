"""
Given an array of integers and an integer k, find out whether there are 
two distinct indices i and j in the array such that nums[i] = nums[j] and 
the difference between i and j is at most k.
"""

def containsNearbyDuplicate(nums, k):
	"""
	:type nums: List[int]
	:type k: int
	:rtype: bool
	"""
	
	dic = {}
	
	for i, n in enumerate(nums):
		if not dic.get(n): dic[n] = [i]
		else: 
			dic[n].append(i)
			vals = dic[n]
			if vals[-1] - vals[-2] <= k: return True
	
	return False
	


