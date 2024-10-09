class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        myDict={}
        for c in magazine:
            if c in myDict.keys():
                myDict[c]+=1
            else:
                myDict.update({c: 1})
        for char in ransomNote:
            if char in myDict.keys():
                if myDict[char] > 0:
                    myDict[char] -= 1
                else:
                    return False
            else:
                return False
        return True
