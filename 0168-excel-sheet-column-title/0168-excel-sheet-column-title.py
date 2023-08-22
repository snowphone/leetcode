class Solution:
    def tochar(self, num):
        return chr( ord('A') + (num) )
    
    def convertToTitle(self, columnNumber: int) -> str:
        answer = []

        while columnNumber:
            columnNumber -= 1  # Make 0-indexed
            answer.append( self.tochar(columnNumber % 26) )
            columnNumber //= 26

        return ''.join(reversed(answer))
