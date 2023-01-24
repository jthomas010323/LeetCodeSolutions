class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[0]=="}" or s[0]==")" or s[0]=="]":
            return False
        valid=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="{" or s[i]=="[":
                valid.append(s[i])
            elif s[i]=="}" and len(valid)>0:
                if valid[len(valid)-1]=="{":
                    valid.pop(len(valid)-1)
                else:
                    return False
            elif s[i]==")" and len(valid)>0:
                if valid[len(valid)-1]=="(":
                    valid.pop(len(valid)-1)
                else:
                    return False
            elif s[i]=="]" and len(valid)>0:
                if valid[len(valid)-1]=="[":
                    valid.pop(len(valid)-1)
                else:
                    return False
            else: 
                return False
        if valid==[]:
            return True
        else:
            return False