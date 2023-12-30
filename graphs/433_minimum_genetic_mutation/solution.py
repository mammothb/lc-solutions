import collections
from typing import List

DIM = 8


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        graph = collections.defaultdict(list)
        for gene in bank:
            if gene == startGene:
                continue
            for i in range(DIM):
                key = f"{gene[:i]}.{gene[i + 1:]}"
                graph[key].append(gene)

        seen = set()
        queue = collections.deque([startGene])
        result = 0
        while queue:
            result += 1
            n_queue = len(queue)
            for _ in range(n_queue):
                gene = queue.popleft()
                seen.add(gene)
                for i in range(DIM):
                    key = f"{gene[:i]}.{gene[i + 1:]}"
                    for next_gene in graph[key]:
                        if next_gene == endGene:
                            return result
                        if next_gene in seen:
                            continue
                        queue.append(next_gene)
        return -1
