class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ""  
        
        for i in range(len(strs[0])):
            print(i)
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return pref
            pref += strs[0][i]
        return pref
    
