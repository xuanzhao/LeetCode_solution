"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in 
the array,and it should return false if every element is distinct.
"""

def containsDuplicate(nums):
	"""
	:type nums: List[int]
	:rtype: bool
	"""
	
	elems = set([])
	
	for item in nums:
		if item in elems: return True
		else: elems.add(item)
	
	return False
	

