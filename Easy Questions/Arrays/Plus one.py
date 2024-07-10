class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s_list =[]
        for i in digits:
            #print(i)
            s_list.append(str(i))
        print(s_list)
        
        output = "".join(s_list)
        print(output)
        res = int(output) + 1
        print(res)
        finalN = str(res)
        print(type(finalN))
        finalList = []
        
        for character in finalN:
            finalList.append(int(character))
            
        return finalList
