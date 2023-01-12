class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word=""
        word_list=[]
        for i in range(len(s)):
            if not s[i]==" ":
                word+=s[i]
                if i==(len(s)-1):
                    word_list.append(word)
            elif s[i]==" " or i==(len(s)-1):
                word_list.append(word)
                word=""
            for i in word_list:
                if i=="":
                    word_list.remove("")
        last_index=len(word_list)-1
        return len(word_list[last_index])
        