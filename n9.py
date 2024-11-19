class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        for i in range(len(str_x)):
            if str_x[i] != str_x[len(str_x) - 1 - i]:
                return False
        return True
