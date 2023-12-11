from typing import List


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        map = {val: i for i, val in enumerate(row)}
        n = len(row)
        i = 0
        count = 0
        # min swap is achieved when we create one couple per swap
        while i < n:
            # Swap only if the current pair isn't a couple, i.e., not
            # 4,5 or 5,4
            if (row[i] % 2 == 0 and row[i + 1] != row[i] + 1) or (
                row[i] % 2 == 1 and row[i + 1] != row[i] - 1
            ):
                if row[i] % 2 == 0:
                    pair_idx = map[row[i] + 1]
                else:
                    pair_idx = map[row[i] - 1]
                map[row[i + 1]] = pair_idx
                row[i + 1], row[pair_idx] = row[pair_idx], row[i + 1]
                count += 1
            i += 2

        return count

    def minSwapsCouples_union_find(self, row: List[int]) -> int:
        def is_couple(n1, n2):
            return (n1 % 2 == 0 and n2 == n1 + 1) or (n1 % 2 == 1 and n2 == n1 - 1)

        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, l, r):
            l_rep = find(parent, l)
            r_rep = find(parent, r)

            if l_rep == r_rep:
                return False
            if l_rep > r_rep:
                l_rep, r_rep = r_rep, l_rep
            parent[r_rep] = l_rep
            return True

        n = len(row)
        parent = {i: i for i in range(n // 2)}
        count = 0
        for i in range(0, n, 2):
            if is_couple(row[i], row[i + 1]):
                continue
            if union(parent, row[i] // 2, row[i + 1] // 2):
                count += 1
        return count
