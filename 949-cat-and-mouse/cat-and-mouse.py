from collections import deque

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        ad_list = graph
        # The state is (m, c, turn), where turn 0 is mouse's turn, 1 is cat's turn
        # We will use BFS starting from known terminal states
        # The color (result) of each state: 0 (draw), 1 (mouse wins), 2 (cat wins)
        color = [[[0] * 2 for _ in range(n)] for __ in range(n)]
        # The degree is the number of possible moves from this state for mouse or cat
        degree = [[[0] * 2 for _ in range(n)] for __ in range(n)]
        
        for mouse in range(n):
            for cat in range(n):
                degree[mouse][cat][0] = len(ad_list[mouse])  # mouse's turn, can move to any adjacent node
                degree[mouse][cat][1] = len(ad_list[cat]) - (0 in ad_list[cat])  # cat's turn, can't move to 0
        
        queue = collections.deque()
        # Initialize terminal states
        for cat in range(n):
            for state in range(2):
                # Mouse wins if it's at 0
                color[0][cat][state] = 1
                queue.append((0, cat, state, 1))
                # Cat wins if cat and mouse are at the same position (not 0)
                if cat != 0:
                    color[cat][cat][state] = 2
                    queue.append((cat, cat, state, 2))
        
        while queue:
            mouse, cat, state, result = queue.popleft()
            # this is the answer
            if (mouse, cat, state) == (1, 2, 0):
                return result
            # Get all parent states that can lead to this state
            if state == 0:  # current turn is mouse's, previous turn was cat's
                for prev_cat in ad_list[cat]:
                    if prev_cat == 0:
                        continue
                    prev_mouse, prev_state = mouse, 1
                    if color[prev_mouse][prev_cat][prev_state] != 0:
                        continue
                    # Cat wants to maximize its chance to win, so if there's a move leading to cat's win (2), then cat will choose it
                    if result == 2:
                        color[prev_mouse][prev_cat][prev_state] = 2
                        queue.append((prev_mouse, prev_cat, prev_state, 2))
                    else:
                        degree[prev_mouse][prev_cat][prev_state] -= 1
                        if degree[prev_mouse][prev_cat][prev_state] == 0:
                            color[prev_mouse][prev_cat][prev_state] = 1
                            queue.append((prev_mouse, prev_cat, prev_state, 1))
            else:  # current turn is cat's, previous turn was mouse's
                for prev_mouse in ad_list[mouse]:
                    prev_cat, prev_state = cat, 0
                    if color[prev_mouse][prev_cat][prev_state] != 0:
                        continue
                    # Mouse wants to maximize its chance to win (1), so if there's a move leading to mouse's win, it will choose it
                    if result == 1:
                        color[prev_mouse][prev_cat][prev_state] = 1
                        queue.append((prev_mouse, prev_cat, prev_state, 1))
                    else:
                        degree[prev_mouse][prev_cat][prev_state] -= 1
                        if degree[prev_mouse][prev_cat][prev_state] == 0:
                            color[prev_mouse][prev_cat][prev_state] = 2
                            queue.append((prev_mouse, prev_cat, prev_state, 2))
        
        return color[1][2][0]