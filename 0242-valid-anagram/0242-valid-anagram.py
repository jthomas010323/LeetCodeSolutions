class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i=''.join(sorted(s))
        j=''.join(sorted(t))
        
        if i==j:
            return True
        else:
            return False