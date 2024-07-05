class Solution:
    def reverse(self, x: int) -> int:
        
        #convert the integer to a list of characters
        numberS = list(str(x))
        print(numberS)
        
        isNegative = False
        if numberS[0] == "-":
            isNegative = True
            numberS.remove("-")
        
        #reverse the list
        numberS.reverse()
        revNumber = int("".join(numberS))
        if isNegative == True:
            revNumber = -revNumber
        
        #checking if it is out of bounds
        if revNumber > 2147483647: 
            return 0
        if revNumber < -2147483648:
            return 0
        print(revNumber)
        return revNumber 
        
