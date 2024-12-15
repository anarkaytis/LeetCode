class Solution:
    def iterate(self, digits: str, prefix: str, result: List[str]) -> None:
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        if digits == "":
            result.append(prefix)
        else:    
            for letter in phone[digits[0]]:
                self.iterate(digits[1:], prefix + letter, result)

    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits != "":
            self.iterate(digits, "", result)
        return result
