class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
	dic = {}
	for i in range(len(nums)):
		complement = target - nums[i]
		if (dic.has_key(complement)):
			return [dic.get(complement), i]
		dic[nums[i]] = i

	return None


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        g = ((i,j+i+1) for i,x in enumerate(nums) for j,y in enumerate(nums[i+1:]) if x+y == target)
        return g.next()