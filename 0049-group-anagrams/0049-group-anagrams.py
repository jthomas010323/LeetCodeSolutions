class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_string=""
        anagram={}
        for word in strs:
            sorted_string = ''.join(sorted(word))
            if sorted_string not in anagram:
                anagram[sorted_string]=[word]
            else:         
                anagram[sorted_string]+=[word]
        return list(anagram.values())

            