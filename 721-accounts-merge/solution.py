from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        emailToAccId = {}
        for accId, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAccId:
                    uf.union(accId, emailToAccId[email])
                else:
                    emailToAccId[email] = accId

        mergedAccounts = defaultdict(list)
        for email, accId in emailToAccId.items():
            mergedAccounts[uf.find(accId)].append(email)

        res = []
        for accId, emails in mergedAccounts.items():
            item = [accounts[accId][0]]
            emails.sort()
            item.extend(emails)
            res.append(item)

        return res


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.root[rootY] = rootX
            self.size[rootX] += self.size[rootY]
