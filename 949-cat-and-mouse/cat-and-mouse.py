CAT_TURN = 0
MOUSE_TURN = 1
CAT = "CAT"
MOUSE = "MOUSE"
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)
        self.n = n
        ad_list = graph
        self.ad_list = ad_list
        self.degrees = self.init_degrees(n, ad_list)
        queue, self.memo = self.init_memo(n)
        while queue:
            mouse, cat, prev_turn = queue.popleft()
            if (mouse, cat, prev_turn) == (1, 2, CAT_TURN):
                return self.memo[mouse][cat][prev_turn]
            self.collect_new_fixed_locations(mouse, cat, prev_turn, queue)
        return 0

    def collect_new_fixed_locations(self, prev_mouse, prev_cat, prev_turn, queue):
        curr_turn = self.get_curr_turn(prev_turn)
        prev_result = self.memo[prev_mouse][prev_cat][prev_turn]
        if prev_turn == MOUSE_TURN:
            for mouse in self.ad_list[prev_mouse]:
                if self.memo[mouse][prev_cat][CAT_TURN] != 0:
                    continue
                elif prev_result == 1:
                    self.memo[mouse][prev_cat][CAT_TURN] = 1
                    queue.append((mouse, prev_cat, CAT_TURN))
                elif prev_result == 2:
                    self.degrees[mouse][prev_cat][CAT_TURN] -= 1
                
                    if self.degrees[mouse][prev_cat][CAT_TURN] == 0:
                        self.memo[mouse][prev_cat][CAT_TURN] = 2
                        queue.append((mouse, prev_cat, CAT_TURN))

        elif prev_turn == CAT_TURN:
            for cat in self.ad_list[prev_cat]:
                if cat == 0:
                    continue
                if self.memo[prev_mouse][cat][MOUSE_TURN] != 0:
                    continue
                elif prev_result == 2:
                    self.memo[prev_mouse][cat][MOUSE_TURN] = 2
                    queue.append((prev_mouse, cat, MOUSE_TURN))
                elif prev_result == 1:
                    self.degrees[prev_mouse][cat][MOUSE_TURN] -= 1
                    if self.degrees[prev_mouse][cat][MOUSE_TURN] == 0:
                        self.memo[prev_mouse][cat][MOUSE_TURN] = 1
                        queue.append((prev_mouse, cat, MOUSE_TURN))
                
        
    def get_curr_turn(self, prev_turn):
        return MOUSE_TURN if prev_turn == CAT_TURN else CAT_TURN


    def init_memo(self, n):
        queue = collections.deque()
        memo = [[[
            0 for a in range(2)]
            for b in range(n)]
            for c in range(n)]
        for cat in range(n):
            for turn in range(2):
                memo[0][cat][turn] = 1
                queue.append((0, cat, turn))
                if cat != 0:
                    memo[cat][cat][turn] = 2
                    queue.append((cat, cat,turn))
        return queue, memo


    def init_degrees(self, n, ad_list):
        degrees = [[[
            0 for a in range(2)]
            for b in range(n)]
            for c in range(n)]
            
        for mouse in range(n):
            for cat in range(n):
                # when positions are mouse, cat and cat is done for moving, how many choices mouse have.
                degrees[mouse][cat][CAT_TURN] = len(ad_list[mouse])
                # when positions are mouse, cat and mouse is done for moving. how many choices cat have.
                degrees[mouse][cat][MOUSE_TURN] = len(ad_list[cat]) - (ad_list[cat].count(0))
                
        return degrees
