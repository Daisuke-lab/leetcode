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
                queue.append((0, cat, state))
                # Cat wins if cat and mouse are at the same position (not 0)
                if cat != 0:
                    color[cat][cat][state] = 2
                    queue.append((cat, cat, state))
        
        while queue:
            mouse, cat, state = queue.popleft()
            result = color[mouse][cat][state]
            is_cat_turn = state == 0
            is_mouse_turn = not is_cat_turn
            # this is the answer
            if (mouse, cat, state) == (1, 2, 0):
                return result
            # Get all parent states that can lead to this state
            if is_cat_turn:  # current turn is mouse's, previous turn was cat's
                for next_cat in ad_list[cat]:
                    if next_cat == 0:
                        continue
                    mouse_turn = 1
                    # if already visited, continue
                    if color[mouse][next_cat][mouse_turn] != 0:
                        continue
                    # if current result is 2, anf after mouse finished moving and position itself at "mouse"
                    # cat can reach out from next_cat to current "cat" position
                    if result == 2:
                        color[mouse][next_cat][mouse_turn] = 2
                        queue.append((mouse, next_cat, mouse_turn))
                    # if there is a selection that leads to mouse's win, you decrease the degree by 1
                    elif result == 1:
                        degree[mouse][next_cat][mouse_turn] -= 1
                        # once it's guaranteed there is no more option (no degree), you mark it as 1
                        if degree[mouse][next_cat][mouse_turn] == 0:
                            color[mouse][next_cat][mouse_turn] = 1
                            queue.append((mouse, next_cat, mouse_turn))
            elif is_mouse_turn:  
                for next_mouse in ad_list[mouse]:
                    cat_turn = 0
                    if color[next_mouse][cat][cat_turn] != 0:
                        continue
                    if result == 1:
                        color[next_mouse][cat][cat_turn] = 1
                        queue.append((next_mouse, cat, cat_turn))
                    elif result == 2:
                        degree[next_mouse][cat][cat_turn] -= 1
                        if degree[next_mouse][cat][cat_turn] == 0:
                            color[next_mouse][cat][cat_turn] = 2
                            queue.append((next_mouse, cat, cat_turn))
        
        # if it is not appended to the queue (neither 1 nor 2), it's 0
        return 0