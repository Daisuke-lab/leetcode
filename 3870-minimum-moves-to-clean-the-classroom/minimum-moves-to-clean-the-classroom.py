class Solution:
    # what do you want to put it into the queue??
    # => (i, j, energy, i_visited, j_visited, litter_count)
    def minMoves(self, classroom: List[str], energy: int) -> int:
        # i, j, energy, i_visited, j_visited
        start_i, start_j, l_map = self.get_start_point(classroom)
        l_count = len(l_map)
        full_energy = energy
        ROW = len(classroom)
        COL = len(classroom[0])
        l_all_visited = (1 << l_count) - 1
        memo = [[[
            -1 for a in range(l_all_visited + 1)]
            for d in range(COL)]
            for e in range(ROW)]
        queue = collections.deque()
        queue.append((start_i, start_j, energy, 0, 0))
        while queue:
            i, j, energy, l_visited, moves = queue.popleft()
            if memo[i][j][l_visited] >= energy:
                    continue
            memo[i][j][l_visited] = energy
            unvisited = False
            if (i, j) in l_map:
                l_index = l_map[(i,j)]
                unvisited = (l_visited & (1 << l_index)) == 0
            if classroom[i][j] == "L" and unvisited:
                l_visited = l_visited | (1 << l_index)

            if l_all_visited == l_visited:
                return moves
            if classroom[i][j] == "R":
                energy = full_energy
            
            

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]

                if energy <= 0:
                    continue
                if new_i < 0 or new_i >= ROW or new_j < 0 or new_j >= COL:
                    continue
                if memo[new_i][new_j][l_visited] >= energy -1:
                    continue
                if classroom[new_i][new_j] == "X":
                    continue
                queue.append((new_i, new_j, energy -1, l_visited, moves + 1))
        return -1                

    def get_start_point(self, classroom):
        start_i = None
        start_j = None
        l_map = {}
        ROW = len(classroom)
        COL = len(classroom[0])
        for i in range(ROW):
            for j in range(COL):
                if classroom[i][j] == "L":
                    l_map[(i, j)] = len(l_map)
                if classroom[i][j] == "S":
                    start_i = i
                    start_j = j
        return start_i, start_j, l_map