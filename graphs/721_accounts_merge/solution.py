import collections
from typing import List


class Solution:
    def accounts_merge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(list)
        # Create a graph of {email: [account IDs]}
        for i, acc_info in enumerate(accounts):
            for email in acc_info[1:]:
                graph[email].append(i)

        def dfs(graph, visited, accounts, acc_id, emails):
            if visited[acc_id]:
                return
            visited[acc_id] = True
            # Whenever we reach a new account ID, we try to add all the emails
            for email in accounts[acc_id][1:]:
                emails.add(email)
                for neighbor in graph[email]:
                    dfs(graph, visited, accounts, neighbor, emails)

        result = []
        visited = [False] * len(accounts)
        for i, acc_info in enumerate(accounts):
            if visited[i]:
                continue
            emails = set()
            dfs(graph, visited, accounts, i, emails)
            result.append([acc_info[0]] + sorted(emails))

        return result

    def accounts_merge_union_find(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(parent, email):
            if parent[email] != email:
                parent[email] = find(parent, parent[email])
            return parent[email]

        def union(parent, l_email, r_email):
            l_rep = find(parent, l_email)
            r_rep = find(parent, r_email)
            if l_rep == r_rep:
                return
            parent[l_rep] = r_rep

        owner = {}
        parent = {}
        for acc_info in accounts:
            for email in acc_info[1:]:
                parent[email] = email
                owner[email] = acc_info[0]
        for acc_info in accounts:
            rep_email = acc_info[1]
            for email in acc_info[1:]:
                union(parent, rep_email, email)
        trees = collections.defaultdict(list)
        for email in parent:
            trees[find(parent, email)].append(email)

        result = [
            [owner[owner_email]] + sorted(emails)
            for owner_email, emails in trees.items()
        ]
        return result

    def accountsMerge_union_find_2(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(parent, i):
            if parent[i] != i:
                parent[i] = find(parent, parent[i])
            return parent[i]

        def union(parent, l, r):
            l_rep = find(parent, l)
            r_rep = find(parent, r)
            if l_rep == r_rep:
                return

            parent[r_rep] = l_rep

        # Stores email->account ID
        # Stores account IDs in parent
        email_to_id = {}
        parent = {}
        for i, account in enumerate(accounts):
            parent[i] = i
            for email in account[1:]:
                email_to_id[email] = i

        for i, account in enumerate(accounts):
            for email in account[1:]:
                union(parent, i, email_to_id[email])

        trees = collections.defaultdict(list)
        for email in email_to_id:
            trees[find(parent, email_to_id[email])].append(email)
        result = []
        for acc_id in trees:
            result.append([accounts[acc_id][0]] + sorted(trees[acc_id]))
        return result
