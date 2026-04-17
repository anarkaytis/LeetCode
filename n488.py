class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = len(startGene)
        visited = set([startGene])
        dq = deque()
        dq.append(startGene)
        bankS = set(bank)
        transitions = 1
        last = startGene
        while len(dq) != 0:
            gene = dq.popleft()
            for i in range(n):
                for letter in "ACGT":
                    mutatedGene = gene[: i] + letter + gene[i + 1 :]
                    if (mutatedGene in bankS) and (mutatedGene not in visited):
                        dq.append(mutatedGene)
                        visited.add(mutatedGene)
                        if mutatedGene == endGene:
                            return transitions
            if gene == last:
                transitions += 1
                if len(dq) != 0:
                    last = dq[-1]
        return -1
