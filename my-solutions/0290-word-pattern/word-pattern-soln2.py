# Inspired by Neetcode solution
class Solution(object):
    def wordPattern(self, pattern, s):
        # pattern: str
        # s: str
        # return type -> bool
        wordList=s.split(" ")

        # edge case: if the number of char in pattern and number of words in s are not equal
        if len(wordList)!=len(pattern):
            return False
        
        wordToChar={}
        charToWord={}

        for word, char in zip(wordList, pattern):
            if word in wordToChar and wordToChar[word]!=char:
                return False
            if char in charToWord and charToWord[char]!=word:
                return False
            
            wordToChar[word]=char
            charToWord[char]=word
        
        return True
