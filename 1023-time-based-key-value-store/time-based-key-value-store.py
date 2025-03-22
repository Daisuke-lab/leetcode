class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, [])
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        pair = self.get_timestamp_prev(key, timestamp)
        value = pair[1] if pair is not None else ""
        return value

    def get_timestamp_prev(self, key: str, timestamp: int) -> int:
        pairs = self.map[key]
        l = 0
        r = len(pairs) - 1
        # Find max timestamp less than timestamp
        timestamp_prev = None
        #print(pairs)
        while l <= r:
            m = (l + r) // 2
            if l == r and pairs[m][0] <= timestamp:
                return pairs[m]
            if pairs[m][0] == timestamp:
                return pairs[m]
            elif pairs[m][0] < timestamp:
                l = m + 1
                timestamp_prev = pairs[m]
            else:
                r = m - 1
        return timestamp_prev
        

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)