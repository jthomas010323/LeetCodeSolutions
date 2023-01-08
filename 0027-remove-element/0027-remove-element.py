class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start_index=0
        end_index=len(nums)-1
        while start_index<=end_index:
            if nums[start_index]==val:
                nums[start_index], nums[end_index]=nums[end_index], nums[start_index]
                end_index-=1
            else:
                start_index+=1
        return start_index