class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        short_word = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]

            if len(word) < len(short_word):
                short_word = word
        
        pref = short_word

        if pref == "":
            return ""

        for word in strs:
            for i in range(len(pref)):
                if pref[i] != word[i]:
                    pref = pref[0:i]
                
                    if pref == "":
                        return ""
                
                    break
        
        return pref
