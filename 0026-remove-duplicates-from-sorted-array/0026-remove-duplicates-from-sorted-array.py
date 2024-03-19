class Solution(object):
    def removeDuplicates(self, nums):
        slow = fast = 0
        while fast < len(nums):
            if nums[slow] == nums[fast]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow+1
                
            
        