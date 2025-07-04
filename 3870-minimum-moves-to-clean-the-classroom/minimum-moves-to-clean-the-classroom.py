class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        full_energy = energy
        ROW = len(classroom)
        COL = len(classroom[0])
        start_point, litters = self.collect_positions(classroom)
        queue = collections.deque()
        all_collected = (1 << len(litters)) -1
        queue.append((start_point[0], start_point[1], 0, energy, 0))
        memo = [[[
            -1 for b in range(all_collected + 1)]
            for c in range(COL)]
            for d in range(ROW)]
        while queue:
            i, j, collected, energy, steps = queue.popleft()
            if i < 0 or j < 0 or i >= ROW or j >= COL:
                continue
            if energy < 0:
                continue
            if classroom[i][j] == "X":
                continue
            if memo[i][j][collected] >= energy:
                continue
            memo[i][j][collected] = energy
            if classroom[i][j] == "R":
                energy = full_energy
            if classroom[i][j] == "L":
                index = litters[(i, j)]
                uncollected = (collected & (1 << index)) == 0
                if uncollected:
                    collected = collected | (1 << index)
            if collected == all_collected:
                return steps
            queue.append((i-1, j, collected, energy -1, steps + 1))
            queue.append((i+1, j, collected, energy -1, steps + 1))
            queue.append((i, j-1, collected, energy -1, steps + 1))
            queue.append((i, j+1, collected, energy -1, steps + 1))
        return -1

    def collect_positions(self, classroom):
        ROW = len(classroom)
        COL = len(classroom[0])
        start_point = None
        litters = {}
        for i in range(ROW):
            for j in range(COL):
                if classroom[i][j] == "S":
                    start_point = (i, j)
                if classroom[i][j] == "L":
                    litters[(i, j)] = len(litters)
        return start_point, litters
