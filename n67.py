class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        lenA = len(a)
        lenB = len(b)
        n = max(lenA, lenB)

        for i in range(1, n + 1):
            sum = carry
            if i <= lenA:
                sum += ord(a[-i]) & 1
            if i <= lenB:
                sum += ord(b[-i]) & 1
            carry = sum >> 1
            result = chr(ord("0") + (sum & 1)) + result
        if carry > 0:
            result = "1" + result
        
        return result
