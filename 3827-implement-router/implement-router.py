class Router:
    # packet_set: duplicate check
    # queue: sending packet
    # heap {destination: queue}: binary search
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.packet_set = set()
        self.queue = collections.deque()
        self.dest_map = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packet_set:
            return False
        if len(self.queue) == self.memoryLimit:
            self.forwardPacket()
        self.packet_set.add((source, destination, timestamp))
        self.queue.append((source, destination, timestamp))
        self.dest_map[destination].append((source, timestamp))
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.packet_set.remove((source, destination, timestamp))
        self.dest_map[destination].pop(0)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        packets = self.dest_map[destination]
        l = 0
        r = len(packets) - 1
        i = None
        while l <= r:
            m = (l + r) // 2
            if packets[m][1] < startTime:
                l = m + 1
            else:
                i = m
                r = m- 1
        if i is None:
            return 0
        l = 0
        r = len(packets) - 1
        j = None
        while l <= r:
            m = (l + r) // 2
            if packets[m][1] <= endTime:
                j = m
                l = m + 1
            else:
                r = m- 1
        if j is None:
            return 0
        return j - i + 1



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)