# My own solution using hashmap
class Solution(object):
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapChar={}
        mapWord={}
        index=0
        space_index=0
        word_count=0
        for i, char in enumerate(s):
            if char==" " or i+1==len(s):
                if i+1==len(s):
                    word=s[space_index:]
                    word_count+=1

                    # edge case: if less words than letters pattern
                    if word_count<len(pattern):
                        return False
                else:
                    word=s[space_index:i]
                    space_index=i+1
                    word_count+=1
                    
                    # edge case: if more words than letters pattern
                    if word_count>=len(pattern):
                        return False
                
                letter=pattern[index]
                
                # check if word is repeated in values
                if letter in mapChar.keys():
                    if mapChar[letter] != word:
                        return False
                else:
                    mapChar[letter]=word
                
                # check if letter is repeated in values
                if word in mapWord.keys():
                    if mapWord[word] != letter:
                        return False
                else:
                    mapWord[word]=letter
                
                index+=1
        
        return True
