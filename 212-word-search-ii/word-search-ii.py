class Trie:
    def __init__(self):
        self.next = {}
        self.is_end = False


class Solution:
    # The last time you solved this similar question, you use backtracking
    # but this time you have list of words
    # Time complexity was O(4^n*m) when the word length is m*n
    # so this quesion's time complexity is O(4^n*m*k) k=the number of words, m=length of word
    # with Trie, you can search with O(k)
    # how long would it take to populate Trie?
    # O(4^n*n) 4^n: traversal of whole board staring with 1 char. n: you do it for all the chcaracters
    # *n: the number of cells
    # if n < m*k => faster to create Trie
    # * you can ignore "search" time complexity because it's really small

    # it's smart to buid Trie with words not with board
    # O(m*k) m: the length of word, k: the number of words
    # n*k
    # 1. loop until you find the first character
    # 2. dig with 4 directions (another function) 
    # 2.5 as args, you want to node (root, i, j, curr)
    # 2.6 if c(i, j) in node.next, pass (node.next, i+di, j+di, curr+c)
    # 2.7 if node.is_end, add to the answer
    # 2.8 if c(i, j) not in node.next, return
    # 3. the output is the list so let's use top down
    # 4. once you reach the is_end, add it to the answer
    # 5. 
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.ROW = len(self.board)
        self.COL = len(self.board[0])
        root = self.buildTrie(words)
        self.answer = set()
        for i in range(self.ROW):
            for j in range(self.COL):
                c = self.board[i][j]
                if c in root.next:
                    self.dig(root, i, j, "", set())
        return list(self.answer)

    def dig(self, node, i, j, curr, passed):
        if node.is_end:
            self.answer.add(curr)
        if i < 0 or i == self.ROW or j < 0 or j == self.COL:
            return
        if (i, j) in passed:
            return
        c = self.board[i][j]
        if c in node.next:
            next_node = node.next[c]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            curr += c
            passed.add((i, j))
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                self.dig(next_node, new_i, new_j,curr, passed)
            passed.remove((i, j))
        

    def buildTrie(self, words):
        root = Trie()
        for word in words:
            self.add(root, word)
        return root

    def add(self, node, word):
        if word == "":
            node.is_end = True
            return 
        c = word[0]
        if c in node.next:
            next_node = node.next[c]
        else:
            next_node = Trie()
            node.next[c] = next_node
        self.add(next_node, word[1:])

        