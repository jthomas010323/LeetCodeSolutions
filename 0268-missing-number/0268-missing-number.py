class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summ=len(nums)*(len(nums)+1)/2
        for i in nums:
            summ-=i
        return summ
        
            
                