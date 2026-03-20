class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev = " "
        cnt_0 = 0
        cnt_1 = 0
        result = 0
        for ch in s:
            if ch == "0":
                if ch == prev:
                    cnt_0 += 1
                else:
                    cnt_0 = 1
                    
                if cnt_0 <= cnt_1:
                    result += 1
            else:
                if ch == prev:
                    cnt_1 += 1
                else:
                    cnt_1 = 1
                    
                if cnt_1 <= cnt_0:
                    result += 1

            prev = ch
        return result
