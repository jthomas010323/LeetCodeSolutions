class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        palindrome=[]
        reverse=[]
        size=len(s)
        for i in range(0, size):
            asci=ord(s[i])
            if (asci<123 and asci>96) or (asci>64 and asci<91) or (asci<58 and asci>47):
                palindrome.append(s[i])
        for k in range(len(palindrome)):
            palindrome[k]=palindrome[k].lower()
        for j in range(len(palindrome)-1, -1, -1):
            reverse.append(palindrome[j])
        if palindrome==reverse:
            return True
        return False