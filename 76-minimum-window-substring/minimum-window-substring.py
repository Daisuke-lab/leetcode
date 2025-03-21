class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Looks like sliding window
        # you always want to start and end with char in t. you don't need to expand further
        # 1. you find the any char to start with (keep shifting to right til then)
        # 2. keep going until you fulfill the condition => how do you know??
        # 3. save the string
        # 4. eliminate suffix and try from 
        # you want to maintain hashmap to count the char (t & s)
        # you also want to maintain match length
        # increment match length when new char count matches t
        # decrement match length when char count less than t
        # stop match length is equal to t1 map key length

        s_map = defaultdict(int)
        t_map = defaultdict(int)
        match_length = 0
        min_substring = ""
        for c in t:
            t_map[c] += 1
        t_map_length = len(t_map)
        i = 0
        j = 0
        while i <= j and j < len(s):
            c = s[j]
            s_map[c] += 1
            if s_map[c] == t_map[c]:
                match_length += 1
            while match_length == t_map_length:
                if len(s[i:j+1]) < len(min_substring) or min_substring == "":
                    min_substring = s[i:j+1]
                start = i
                while (start == i) or (i < len(s) and s[i] not in t):
                    removing_c = s[i]
                    if s_map[removing_c] == t_map[removing_c]:
                        match_length -= 1
                    s_map[removing_c] -= 1
                    i += 1
            j += 1
        return min_substring
        