class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic = {}
        result=[]
        if len(nums1)>len(nums2):
            for i in range(len(nums2)):
                dic[nums2[i]] = 0
            for j in range(len(nums1)):
                if nums1[j] in dic:
                    dic[nums1[j]]+=1
            for k in dic:
                if dic[k]>0:
                    result.append(k)
        else:
            for i in range(len(nums1)):
                dic[nums1[i]] = 0
            for j in range(len(nums2)):
                if nums2[j] in dic:
                    dic[nums2[j]]+=1
            for k in dic:
                if dic[k]>0:
                    result.append(k)
        return result