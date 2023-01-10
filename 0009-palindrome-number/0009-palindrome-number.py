class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        backward=[]
        newword=''
        x=str(x)
        for i in range(len(x)-1, -1, -1):
            backward.append(x[i])
        
        for character in backward:
            newword+=character
        if newword==x:
            return True
        return False