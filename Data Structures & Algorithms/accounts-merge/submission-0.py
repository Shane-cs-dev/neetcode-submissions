class UnionFind:
    def __init__(self, n):
        self._parent = [i for i in range(n)]
        self._rank = [1] * n
    
    def find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self.find(self._parent[x])
        return self._parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # Check the rank and merge them
        if self._rank[px] > self._rank[py]:
            self._parent[py] = px
        elif self._rank[py] > self._rank[px]:
            self._parent[px] = py
        else:
            self._parent[px] = py
            self._rank[py] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create an UnionFind
        uf = UnionFind(len(accounts))
        email_to_acc = {} # Map the account to the index of the account

        # Map the email to the name (account)
        for idx, sub_account in enumerate(accounts):
            for email in sub_account[1:]:
                if email in email_to_acc: # If there's email match to other account already exist in the email_to_acc
                    uf.union(idx, email_to_acc[email])
                else:
                    email_to_acc[email] = idx
        
        # for key, value in email_to_acc.items():
        #     print(f"{key}: {value}")
        # for parent in uf._parent:
        #     print(f"{parent}")

        email_group = defaultdict(list) # index of acc to list of emails
        for email, acc_idx in email_to_acc.items():
            leader = uf.find(acc_idx) # Find the parent
            email_group[leader].append(email)
        

        res = []
        for i, emails in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(email_group[i]))
        return res
