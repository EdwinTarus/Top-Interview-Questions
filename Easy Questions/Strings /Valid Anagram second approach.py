class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Checking the lenghts
        if len(s) != len(t):
            return False
        
        # Initializing the dictionaries
        sDict = {}
        tDict = {}
        
        # checking if the characters are in the dictionaries 
        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] +=1
            else:
                sDict[s[i]] = 1
            
            if t[i] in tDict:
                tDict[t[i]] +=1
            else:
                tDict[t[i]] = 1
        
        print(tDict) 
        print(sDict)
        if sDict != tDict:
            return False
        
        return True
