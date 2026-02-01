class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.Leaf = None

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        trans = namedtuple('trans', ['len', 'src', 'dst', 'cost'])
        INF = 20000000000
        id_cnt = 0
        id = {}
        n = len(original)
        grouped = []
        for i in range(n):
            grouped.append(trans(len(original[i]), original[i], changed[i], cost[i]))
        grouped.sort(key=lambda x: x.len)
        
        #hash
        len_list = []
        for i in range(n):
            if grouped[i].src not in id:
                id[grouped[i].src] = id_cnt 
                id_cnt += 1
                len_list.append(grouped[i].len)
            if grouped[i].dst not in id:
                id[grouped[i].dst] = id_cnt 
                id_cnt += 1
                len_list.append(grouped[i].len)
        
        #Floyd Warshall 
        fw = [[INF] * id_cnt for _ in range(id_cnt)]
        for i in range(id_cnt):
            fw[i][i] = 0
        for i in range(n):
            fw[id[grouped[i].src]][id[grouped[i].dst]] = min(fw[id[grouped[i].src]][id[grouped[i].dst]], grouped[i].cost)
        
        indexes = [0]
        for i in range(1, id_cnt):
            if len_list[i] != len_list[i - 1]:
                indexes.append(i)
        indexes.append(id_cnt)

        for l in range(1, len(indexes)):
            for k in range(indexes[l - 1], indexes[l]):
                for i in range(indexes[l - 1], indexes[l]):
                    if fw[i][k] != INF: 
                        for j in range(indexes[l - 1], indexes[l]):
                            fw[i][j] = min(fw[i][j], fw[i][k] + fw[k][j])

        root = TrieNode()
        for s, s_id in id.items():
            curr = root
            for c in s:
                idx = ord(c) - ord('a')
                if curr.children[idx] is None:
                    curr.children[idx] = TrieNode()
                curr = curr.children[idx]
            curr.Leaf = s_id
        
        #dynamic programmig
        m = len(source)
        dp = [INF] * (m + 1)
        dp[m] = 0
        for i in range(m - 1, -1, -1):
            if source[i] == target[i]:
                dp[i] = dp[i + 1]
            s_curr = root
            t_curr = root
            for j in range(i, m):
                s_curr = s_curr.children[ord(source[j]) - ord('a')]
                t_curr = t_curr.children[ord(target[j]) - ord('a')]
                if (s_curr is None) or (t_curr is None):
                    break
                if (s_curr.Leaf is not None) and (t_curr.Leaf is not None):
                    dp[i] = min(dp[i], fw[s_curr.Leaf][t_curr.Leaf] + dp[j + 1])
        
        return dp[0] if dp[0] != INF else -1
