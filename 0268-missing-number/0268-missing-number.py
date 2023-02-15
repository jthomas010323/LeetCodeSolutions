class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j=len(nums)
        summ=j*(j+1)/2
        for i in nums:
            summ-=i
        return summ
        
            
                