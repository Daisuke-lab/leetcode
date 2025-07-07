class Solution:
    # Dijkstra
    # how do you define infinite
    # if it exceeds sy, sx, you can discard it
    # heap or queue? as long as it doesn't exceed tx, ty, it is equally getting close
    # => so queue is enough

    # How about greedy?
    # tx - sx = x_gap. you have to fill this out by adding m
    # x + max(x + max(x, y), y)
    # Eventually, tx = x + x + x + x ... + y + y... = ax + by
    # ty = cx + dy

    # Reverse Thinking tx to sx
    # (x, y, curr_max) => doesn't help you much
    def minMoves(self, sx: int, sy: int, tx: int, ty: int) -> int:
        if sx == tx and sy == ty:
            return 0
        if max(sx, sy) == 0:
            return -1
            
        steps = 0
        while (sx, sy) != (tx, ty):
            if sx > tx or sy > ty:
                return -1
            steps += 1
            tx, ty = self.get_last_position(tx, ty, sx, sy)
            #print(tx, ty)
        return steps if (sx, sy) == (tx, ty) else -1

    def get_last_position(self, x, y, sx, sy):
        # because you add max to x or y
        # (x + max(prev_x, prev_y), y) or (y + max(prev_x, prev_y))
        # Either way, the one you added m to is always bigger.
        
        # Previsouly you added m to x 
        if x > y:
            # x + y
            prev_x = x - y
            if max(prev_x, y) == y:
                return prev_x, y
            # x + x
            # it can not be float 
            if x % 2 != 0:
                return -1, -1
            prev_x = x // 2
            if max(prev_x, y) == prev_x:
                return prev_x, y
        elif x < y:
            # x + y
            prev_y = y - x
            if max(prev_y, x) == x:
                return x, prev_y
            # y + y
            # it can not be float
            if y % 2 != 0:
                return -1, -1
            prev_y = y //2
            if max(prev_y, x) == prev_y:
                return x, prev_y
        else:
            # if x == y, prev can be either (0, y) or (x, 0)
            if sx == 0:
                return 0, y
            if sy == 0:
                return x, 0
            else:
                return -1, -1
        return -1, -1
            