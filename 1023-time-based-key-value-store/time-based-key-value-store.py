class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.store[key]
        value = ""
        l = 0
        r = len(data) - 1
        while l <= r:
            m = (l + r) // 2
            if data[m][0] == timestamp:
                value = data[m][1]
                break
            elif data[m][0] < timestamp:
                value = data[m][1]
                l = m + 1
            else:
                r = m - 1
        return value

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)