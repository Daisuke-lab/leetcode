class Solution:
    # Brute force
    # try all possible patterns
    # orders matters so almost infinite

    # DP
    # how do you want to make small problems
    # you can not
    # Digit DP (but you need to go back to the prev sometimes)
    
    # graph
    # 
    def openLock(self, deadends: List[str], target: str) -> int:
        min_heap = [(0, 0, "0000")]
        visited = set()
        dead_ends = set(deadends)
        
        while min_heap:
            operation, distance, slot = heapq.heappop(min_heap)
            if slot in dead_ends:
                continue
            if slot == target:
                return operation
            if slot in visited:
                continue
            visited.add(slot)
            next_slots = self.get_next_slots(slot)
            for next_slot in next_slots:
                if next_slot in visited:
                    continue
                next_distance = self.calculate_distance(next_slot, target)
                heapq.heappush(min_heap, (operation + 1, next_distance, next_slot))
        return -1

    def get_next_slots(self, slot):
        next_slots = []
        for i in range(4):
            n = int(slot[i])
            if n == 0:
                next_slots.append(f"{slot[:i]}1{slot[i+1:]}")
                next_slots.append(f"{slot[:i]}9{slot[i+1:]}")
            elif n == 9:
                next_slots.append(f"{slot[:i]}0{slot[i+1:]}")
                next_slots.append(f"{slot[:i]}8{slot[i+1:]}")
            else:
                next_slots.append(f"{slot[:i]}{n-1}{slot[i+1:]}")
                next_slots.append(f"{slot[:i]}{n+1}{slot[i+1:]}")
        return next_slots
                


    def calculate_distance(self, slot, target):
        distance = 0
        for i in range(4):
            n = int(slot[i])
            t = int(target[i])
            if (n == 0 and t == 9) or (n == 9 and t == 0):
                distance += 1
            else:
                distance += abs(n - t)
        return distance