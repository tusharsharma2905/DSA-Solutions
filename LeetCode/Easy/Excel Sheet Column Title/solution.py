class Solution(object):
    def convertToTitle(self, columnNumber):
        chars = []
        
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            chars.append(chr(ord('A') + remainder))
            columnNumber //= 26
            
        return "".join(chars[::-1])