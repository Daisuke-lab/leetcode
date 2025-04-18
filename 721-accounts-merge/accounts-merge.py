class UnionFind:

    def __init__(self, accounts):
        self.names = []
        self.emails_list = []
        for account in accounts:
            name = account[0]
            emails = set(account[1:])
            self.names.append(name)
            self.emails_list.append(emails)
        self.parents = [i for i in range(len(accounts))]

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node
    
    def union(self, node1, node2):
        node1_parent = self.find(node1)
        node2_parent = self.find(node2)
        if node1_parent == node2_parent:
            return 
        node1_emails = self.emails_list[node1_parent]
        node2_emails = self.emails_list[node2_parent]
        if len(node1_emails & node2_emails)== 0:
            return
        if len(node1_emails) < len(node2_emails):
            node1_parent, node2_parent = node2_parent, node1_parent
            node1_emails, node2_emails = node2_emails, node1_emails
        node1_emails = node1_emails | node2_emails
        self.emails_list[node1_parent] = node1_emails
        self.emails_list[node2_parent] = set()
        self.parents[node2_parent] = node1_parent



class Solution:
    # 1. init union find (easy)
    # 1.1 you don't need size, but make sure you update parent list
    # 2. collect edges
    # 3. merge
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = UnionFind(accounts)
        for i in range(len(accounts)-1):
            for j in range(i+1, len(accounts)):
                union_find.union(i, j)
        #print(union_find.emails_list)
        answers = []
        for i, emails in enumerate(union_find.emails_list):
            if len(emails) > 0:
                name = union_find.names[i]
                answer = [name] + sorted(list(emails))
                answers.append(answer)
        return answers
        