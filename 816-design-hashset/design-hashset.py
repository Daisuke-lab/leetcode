class MyHashSet:

    def __init__(self):
        self.hash_map = {}

    def add(self, key: int) -> None:
        self.hash_map[key]= "DUMMY"

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            del self.hash_map[key]

    def contains(self, key: int) -> bool:
        return key in self.hash_map


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)