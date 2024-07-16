class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # check if needle is empty 
        if needle == "":
            return 0

        index = haystack.find(needle)
        if index != 10^5:
            return index 
        
        else:
            return -1
