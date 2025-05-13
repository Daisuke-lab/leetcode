class Solution:
    # you want to start any char in t
    # you want to continue all the way til the requirement is fulfilled
    # once it reaches, you are going to pop it til the next char in t
    def minWindow(self, s: str, t: str) -> str:
        answer = None
        i = 0
        j = 0
        count_map = self.init_count_map(t)
        done = 0
        t_count = len(count_map)
        move_forward = True
        while j < len(s):
            if t_count == done:
                #print(len(answer) if answer is not None else "None", j - i + 1)
                if answer is None:
                    answer = s[i:j+1]
                elif len(answer) > (j - i + 1):
                    answer = s[i:j+1]
                removing_c = s[i]
                i += 1
                if removing_c in count_map:
                    count_map[removing_c] += 1
                    if count_map[removing_c] == 1:
                        done -= 1
                        j += 1
                while i < j and s[i] not in count_map:
                    i += 1
            else:
                c = s[j]
                if c in count_map:
                    count_map[c] -= 1
                    if count_map[c] == 0:
                        done += 1
                if t_count != done:
                    j += 1
        return answer if answer is not None else ""



    def init_count_map(self, t):
        count_map = {}
        for c in t:
            count_map[c] = count_map.get(c, 0) + 1
        return count_map
        