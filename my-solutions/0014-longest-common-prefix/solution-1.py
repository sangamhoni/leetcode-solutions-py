class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        common_char = strs[0]
        
        for i in range(1, len(strs)):
            word = strs[i]

            loop = min((len(word), len(common_char)))
            common_char = common_char[0:loop]

            for j in range(loop):
                if word[j] != common_char[j]:
                    print(common_char)
                    common_char = common_char[0:j]

                    break
                    
        return common_char
    