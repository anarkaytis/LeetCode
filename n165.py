class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v_0 = version1.split('.')
        v_1 = version2.split('.')
        for i in range(max(len(v_0), len(v_1))):
            v0 = int(v_0[i]) if i < len(v_0) else 0 
            v1 = int(v_1[i]) if i < len(v_1) else 0 
            if v0 != v1:
                return -1 if v0 < v1 else 1
        return 0
