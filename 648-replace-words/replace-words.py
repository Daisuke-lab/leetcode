class Trie:
    def __init__(self):
        self.next = {}
        self.is_end = False

    def build(self, dictionary):
        for word in dictionary:
            self.insert(word)
        return self
                
    def insert(self, word):
        if word == "":
            self.is_end = True
            return
        if word[0] in self.next:
            node = self.next[word[0]]
            node.insert(word[1:])
        else:
            node = Trie()
            self.next[word[0]] = node
            node.insert(word[1:])
    
    def search(self, word):
        original_word = word
        queue = collections.deque()
        queue.append((self, word, ""))
        while queue:
            node, word, curr = queue.popleft()
            if node.is_end:
                return curr
            if word != "":
                c = word[0]
                if c in node.next:
                    next_node = node.next[c]
                    queue.append((next_node, word[1:], curr + c))
                else:
                    return original_word
            else:
                original_word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie().build(dictionary)
        answer = []
        for word in sentence.split(" "):
            root = trie.search(word)
            if root is None:
                answer.append(word)
            else:
                answer.append(root)
        return " ".join(answer)