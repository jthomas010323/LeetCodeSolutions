class Solution(object):
    def removeDuplicates(self, nums):
        i=0
        for k in range(1,len(nums)):    
            if nums[i] != nums[k]:  
                nums[i+1] = nums[k]
                i+=1
        return(i+1)
                
            
        