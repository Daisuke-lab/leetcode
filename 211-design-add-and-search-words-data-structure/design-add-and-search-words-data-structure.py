class Trie:
    def __init__(self):
        self.is_end = False
        self.next = {}

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.add(word, self.root)

    def add(self, word, node):
        if word == "":
            node.is_end = True
            return
        if word[0] in node.next:
            next_node = node.next[word[0]]
        else:
            next_node = Trie()
            node.next[word[0]] = next_node
        self.add(word[1:], next_node)
        

    def search(self, word: str) -> bool:
        return self.research(word, self.root)
    def research(self, word, node):
        if word == "":
            if node.is_end:
                return True
            else:
                return False
        if word[0] in node.next:
            return self.research(word[1:], node.next[word[0]])
        elif word[0] == ".":
            result = False
            for next_node in node.next.values():
                result = self.research(word[1:], next_node) or result
                if result:
                    return True
            return result
        else:
            return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)