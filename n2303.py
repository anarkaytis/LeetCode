class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        result = 0
        prev = 0
        for bracket in brackets:
            taxed_income = min(income, bracket[0]) - prev
            result += taxed_income * bracket[1] / 100
            prev = bracket[0]
            if income < bracket[0]:
                break
        return result   
