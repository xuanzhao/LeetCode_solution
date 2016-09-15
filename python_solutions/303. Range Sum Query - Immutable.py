class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.dp = self.NumArray()

    def NumArray(self):
        dp = self.nums
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] + self.nums[i]
        return dp
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return (self.dp[j] - self.dp[i-1] if i>0 else self.dp[j])

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i <= j and i>=0 and j < len(self.nums):
            return self.nums[i:j+1]
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
















