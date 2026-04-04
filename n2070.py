class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText) // rows
        result = ""
    
        for j in range(n):
            x = 0
            y = j
            while (x < rows) and (y < n):
                result += encodedText[x * n + y]
                x += 1
                y += 1
        
        return result.rstrip()
