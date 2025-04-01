class Solution:
    # worse case could be O(2^n). *you can either choose the first char of s1 or s2 and dig it until the end

    # make grid with s1 length + 1 and s2 length + 1
    # start with grid[len(s1)][len(s2) -1] or grid[len(s1) -1][len(s2)]
    # you can go up or left
    # you want to put s3 index into grid
    # create queue to add (i, j, s3_i)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        visited = set()
        queue = collections.deque()
        if s3 == "":
            if s1 == "" and s2 == "":
                return True
            else:
                return False
            
        if len(s1) != 0 and s1[-1] == s3[-1]:
            queue.append((len(s1) -1, len(s2), len(s3)-1))
        if len(s2) != 0 and s2[-1] == s3[-1]:
            queue.append((len(s1), len(s2) - 1, len(s3) -1))
        while queue:
            i, j, s3_i = queue.popleft()
            if (i, j) == (0, 0) and s3_i == 0:
                return True
            # you use all chars in s1 and s2 but s3 in remaining
            if (i, j) == (0, 0):
                return False
            # s3 is out of index but you still have s1 or s2
            if s3_i == 0:
                return False
            if (i, j) in visited:
                continue
            visited.add((i, j))
            next_c = s3[s3_i-1]
            if i > 0 and s1[i-1] == next_c:
                queue.append((i-1, j, s3_i-1))
            if j > 0 and s2[j-1] == next_c:
                queue.append((i, j-1, s3_i-1))
            


        return False
        