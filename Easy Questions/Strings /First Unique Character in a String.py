class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        countchar = {}
        
        for i in s:
            if i in countchar:
                countchar[i] +=1
            else:
                countchar[i] =1 
        for i, char in enumerate(s):
            if countchar[char] == 1:
                return i
            
        return -1
        
        
# Solution two        
#         count = defaultdict(int)
        
#         for c in s:
#             count[c] += 1
#         # print(count)
        
#         for i, c in enumerate(s):
#             if count[c] == 1:
#                 return i
#         return -1
