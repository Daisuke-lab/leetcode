class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # you can not cut in the middle of rectangle
        # I can say dividing line is always aligned with rectangle (it doesn't have to be)
        # you can not cut the edge (eg. you can cut n)
        
        # you can make a grid n/n O(n^2)
        # and change rectangle space to change number (i) O(n^2) in worst case
        # andh check all possible lines O(n^2) if i and i + 1 is differnt number it's ok
        #  Time complexity is O(n^2)
        # I think it's optimized
        
        # you extract (xi, xj) and sort it. if xj <= next xj => divisble
        
        xs = []
        ys = []
        for rectangle in rectangles:
            xs.append((rectangle[0], rectangle[2]))
            ys.append((rectangle[1], rectangle[3]))
        xs.sort()
        count = 0
        curr_max = 0
        for i in range(0, len(xs) -1):
            curr_x1, curr_x2 = xs[i]
            next_x1, next_x2 = xs[i+1]
            curr_max = max(curr_max, curr_x2)
            if curr_max <= next_x1:
                count += 1
                if count == 2:
                    return True
        ys.sort()
        count = 0
        curr_max = 0
        for i in range(0, len(ys) -1):
            curr_y1, curr_y2 = ys[i]
            next_y1, next_y2 = ys[i+1]
            curr_max = max(curr_max, curr_y2)
            if curr_max <= next_y1:
                count += 1
                if count == 2:
                    return True
        return False

        