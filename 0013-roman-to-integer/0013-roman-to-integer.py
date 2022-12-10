class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        i=0
       
        table = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        while i<=(len(s)-1):
            if i==len(s)-1:
                sum=sum+table.get(s[i])
                return sum
            if table.get(s[i])<table.get(s[i+1]):
                sum=sum-table.get(s[i])
                print(i)
                i=i+1
            else:
                sum=sum+table.get(s[i])
                i=i+1
                print(i)