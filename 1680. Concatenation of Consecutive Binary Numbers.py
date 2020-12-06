class Solution:
    def concatenatedBinary(self, n: int) -> int:
        
        def binaryToDecimal(n): 
            return int(n,2)
        
        def decimalToBinary(n):  
            return bin(n).replace("0b", "")
        
        arg = ''
        
        for i in range(1, n + 1):
            arg += decimalToBinary(i)
            
        return binaryToDecimal(arg) % (10 ** 9 + 7)
        
            
      