from collections import deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        # The state is (m, c, turn), where turn 0 is mouse's turn, 1 is cat's turn
        # We will use BFS starting from known terminal states
        # The color (result) of each state: 0 (draw), 1 (mouse wins), 2 (cat wins)
        color = [[[0] * 2 for _ in range(n)] for __ in range(n)]
        # The degree is the number of possible moves from this state for mouse or cat
        degree = [[[0] * 2 for _ in range(n)] for __ in range(n)]
        
        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])  # mouse's turn, can move to any adjacent node
                degree[m][c][1] = len(graph[c]) - (0 in graph[c])  # cat's turn, can't move to 0
        
        q = deque()
        # Initialize terminal states
        for i in range(n):
            for t in range(2):
                # Mouse wins if it's at 0
                color[0][i][t] = 1
                q.append((0, i, t, 1))
                # Cat wins if cat and mouse are at the same position (not 0)
                if i != 0:
                    color[i][i][t] = 2
                    q.append((i, i, t, 2))
        
        while q:
            m, c, t, res = q.popleft()
            if (m, c, t) == (1, 2, 0):
                return res
            # Get all parent states that can lead to this state
            if t == 0:  # current turn is mouse's, previous turn was cat's
                for prev_c in graph[c]:
                    if prev_c == 0:
                        continue
                    prev_m, prev_t = m, 1
                    if color[prev_m][prev_c][prev_t] != 0:
                        continue
                    # Cat wants to maximize its chance to win, so if there's a move leading to cat's win (2), then cat will choose it
                    if res == 2:
                        color[prev_m][prev_c][prev_t] = 2
                        q.append((prev_m, prev_c, prev_t, 2))
                    else:
                        degree[prev_m][prev_c][prev_t] -= 1
                        if degree[prev_m][prev_c][prev_t] == 0:
                            color[prev_m][prev_c][prev_t] = 1
                            q.append((prev_m, prev_c, prev_t, 1))
            else:  # current turn is cat's, previous turn was mouse's
                for prev_m in graph[m]:
                    prev_c, prev_t = c, 0
                    if color[prev_m][prev_c][prev_t] != 0:
                        continue
                    # Mouse wants to maximize its chance to win (1), so if there's a move leading to mouse's win, it will choose it
                    if res == 1:
                        color[prev_m][prev_c][prev_t] = 1
                        q.append((prev_m, prev_c, prev_t, 1))
                    else:
                        degree[prev_m][prev_c][prev_t] -= 1
                        if degree[prev_m][prev_c][prev_t] == 0:
                            color[prev_m][prev_c][prev_t] = 2
                            q.append((prev_m, prev_c, prev_t, 2))
        
        return color[1][2][0]