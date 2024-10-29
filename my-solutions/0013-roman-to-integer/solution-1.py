class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        r2i = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        prev = r2i[s[0]]

        num = 0
        
        for i in range(1, len(s)):
            if prev < r2i[s[i]]:
                num -= prev
            else:
                num += prev
            prev = r2i[s[i]]
        
        num += prev
        return num
